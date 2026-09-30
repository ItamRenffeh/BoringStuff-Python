import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

def obtener_noticias_ciberseguridad():
    """
    Realiza web scraping en The Hacker News para obtener los últimos artículos.
    """
    url = "https://thehackernews.com/"
    # El User-Agent simula ser un navegador real para evitar bloqueos básicos
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    
    print(f"[*] Conectando a {url} ...")
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"[-] Error al conectar: {e}")
        return []

    # Convertimos el texto HTML crudo en un objeto navegable
    soup = BeautifulSoup(response.text, 'html.parser')
    noticias = []
    
    # Inspeccionando el HTML de la página, sabemos que cada noticia 
    # está envuelta en una etiqueta <a> con la clase 'story-link'
    articulos = soup.find_all('a', class_='story-link')

    # Tomamos solo las 5 noticias más recientes
    for articulo in articulos[:5]:
        try:
            # Extraemos el texto de las etiquetas internas usando sus clases CSS
            titulo = articulo.find('h2', class_='home-title').text.strip()
            resumen = articulo.find('div', class_='home-desc').text.strip()
            enlace = articulo['href']
            
            noticias.append({
                "fecha": datetime.now().strftime("%Y-%m-%d"),
                "titulo": titulo,
                "resumen": resumen,
                "enlace": enlace
            })
        except AttributeError:
            # Si alguna noticia no tiene el formato esperado, la saltamos
            continue
            
    return noticias

def main():
    noticias = obtener_noticias_ciberseguridad()
    
    if not noticias:
        print("[-] No se encontraron noticias.")
        return

    # Generamos un nombre de archivo dinámico con la fecha de hoy
    fecha_hoy = datetime.now().strftime("%Y-%m-%d")
    nombre_archivo = f"OSINT_Reporte_{fecha_hoy}.csv"

    encabezados = ["fecha", "titulo", "resumen", "enlace"]

    # Guardamos en CSV
    with open(nombre_archivo, mode='w', newline='', encoding='utf-8') as archivo_csv:
        escritor = csv.DictWriter(archivo_csv, fieldnames=encabezados)
        escritor.writeheader()
        escritor.writerows(noticias) # Escribe toda la lista de diccionarios de una vez

    print("\n[+] Resumen de noticias extraídas:")
    print("-" * 70)
    for i, noti in enumerate(noticias, 1):
        print(f"{i}. {noti['titulo']}")
    
    print("-" * 70)
    print(f"[+] Reporte OSINT guardado en: {nombre_archivo}")

if __name__ == "__main__":
    main()