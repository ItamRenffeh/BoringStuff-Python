import sys
import requests

# 1. Definimos la ciudad. Usa sys.argv si la escribís en consola, o Bahía Blanca por defecto para la macro.
if len(sys.argv) > 1:
    ciudad = " ".join(sys.argv[1:])
else:
    ciudad = "Bahia Blanca"

print(f"Consultando el satélite para {ciudad.title()}...\n")

try:
    # 2. Hacemos la petición a la API pidiendo formato JSON (?format=j1)
    url = f"https://wttr.in/{ciudad}?format=j1"
    
    # Aplicamos un timeout de 10 segundos y el chequeo de errores del Capítulo 13
    respuesta = requests.get(url, timeout=10)
    respuesta.raise_for_status()
    
    # 3. Convertimos el JSON descargado a un diccionario nativo de Python
    datos = respuesta.json()
    
    # 4. Navegamos por el diccionario para extraer los datos quirúrgicamente
    condicion_actual = datos['current_condition'][0]
    clima_hoy = datos['weather'][0]
    
    temp_actual = condicion_actual['temp_C']
    viento = condicion_actual['windspeedKmph']
    temp_max = clima_hoy['maxtempC']
    temp_min = clima_hoy['mintempC']
    
    # La API divide el día en 8 franjas horarias. Tomamos el índice [4] (aprox. 12:00 PM) para la lluvia
    prob_lluvia = clima_hoy['hourly'][4]['chanceofrain'] 
    
    # 5. Imprimimos el panel final en la consola
    print("=" * 35)
    print(f" 📍 {ciudad.title().upper()}")
    print("=" * 35)
    print(f" 🌡️  Temperatura:  {temp_actual}°C")
    print(f" 📉 Mín / Máx:    {temp_min}°C / {temp_max}°C")
    print(f" 💨 Viento:       {viento} km/h")
    print(f" 🌧️  Prob. Lluvia: {prob_lluvia}% (Mediodía/Tarde)")
    print("=" * 35)

except requests.exceptions.RequestException as error:
    print(f"Error de conexión: {error}")
except KeyError:
    print(f"Error: La API no reconoció la ciudad '{ciudad}'.")