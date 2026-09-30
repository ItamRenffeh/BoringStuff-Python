import requests
import xml.etree.ElementTree as ET

def obtener_clima(ciudad="Bahia Blanca"):
    print("\n" + "=" * 50)
    print(f" 📍 CLIMA DE HOY: {ciudad.upper()}")
    print("=" * 50)
    try:
        url = f"https://wttr.in/{ciudad}?format=j1"
        res = requests.get(url, timeout=10)
        res.raise_for_status()
        
        datos = res.json()
        condicion = datos['current_condition'][0]
        hoy = datos['weather'][0]
        
        print(f" 🌡️  Actual:       {condicion['temp_C']}°C")
        print(f" 📉 Mín / Máx:    {hoy['mintempC']}°C / {hoy['maxtempC']}°C")
        print(f" 💨 Viento:       {condicion['windspeedKmph']} km/h")
        print(f" 🌧️  Prob. Lluvia: {hoy['hourly'][4]['chanceofrain']}% (Mediodía/Tarde)")
    except Exception as e:
        print(f" No se pudo cargar el clima. Error: {e}")

def obtener_noticias(titulo_seccion, url_rss, limite=5):
    print("\n" + "=" * 50)
    print(f" 📰 {titulo_seccion}")
    print("=" * 50)
    try:
        # Descargamos el archivo XML de noticias
        res = requests.get(url_rss, timeout=10)
        res.raise_for_status()
        
        # Convertimos el texto descargado en un Árbol (similar a Beautiful Soup)
        arbol = ET.fromstring(res.content)
        
        # Buscamos todas las etiquetas <item> (que representan cada noticia)
        articulos = arbol.findall('.//item')
        
        # Iteramos solo hasta el límite que pediste (5)
        for i, articulo in enumerate(articulos[:limite], 1):
            titulo = articulo.find('title').text
            link = articulo.find('link').text
            print(f"{i}. {titulo}")
            print(f"   🔗 {link}\n")
            
    except Exception as e:
        print(f" No se pudieron cargar las noticias. Error: {e}")

def main():
    print("Iniciando escaneo de servidores...\n")
    
    # 1. Ejecutar módulo del clima
    obtener_clima()
    
    # 2. Noticias Globales (Google News RSS - Mundo)
    obtener_noticias(
        "NOTICIAS GLOBALES (Top 5)",
        "https://news.google.com/rss/headlines/section/topic/WORLD?hl=es-419&gl=AR&ceid=AR:es-419"
    )
    
    # 3. Noticias Argentina (Google News RSS - Argentina)
    obtener_noticias(
        "NOTICIAS ARGENTINA (Top 5)",
        "https://news.google.com/rss?hl=es-419&gl=AR&ceid=AR:es-419"
    )
    
    # 4. Ciberseguridad (Feed de ESET Security en Español)
    # Si preferís en inglés (The Hacker News), podés usar: https://feeds.feedburner.com/TheHackersNews
    obtener_noticias(
        "CIBERSEGURIDAD Y REDES (Top 5)",
        "https://www.welivesecurity.com/la-es/feed/"
    )

if __name__ == "__main__":
    main()