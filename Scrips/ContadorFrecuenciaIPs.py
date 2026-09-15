

def es_ip_valida(ip):
    # Divide la IP en sus cuatro partes usando el punto como separador.
    partes = ip.strip().split(".")

    
    if len(partes) != 4:
        return False

    
    if any(not parte.isdigit() for parte in partes):
        return False

    # Convierte cada parte de texto a un número entero.
    octetos = [int(parte) for parte in partes]

    
    return all(0 <= octeto <= 255 for octeto in octetos)

def cantidad_apariciones(Lista_ip):
    diccionario_ips = {}

    
    for ip in Lista_ip:
        ip = ip.strip()

        # Solo agrega al diccionario las IPs que cumplen las reglas de IPv4.
        if es_ip_valida(ip):
            # Luego suma una aparición y guarda el resultado en el diccionario.
            diccionario_ips[ip] = diccionario_ips.get(ip, 0) + 1

  
    return diccionario_ips
            
       
def mostrar_resultado(diccionario_ips):
    # items() obtiene pares en la forma (clave, valor), por ejemplo:
    # ("8.8.8.8", 3).
    # sorted() recibe esos pares y crea una nueva lista ordenada.
    # key indica qué parte de cada par se usará para ordenar.
    # lambda x: x[1] es una función pequeña: recibe un par x y devuelve
    # su segundo elemento, que en este caso es la cantidad de apariciones.
    # reverse=True ordena de mayor a menor cantidad.
    ordenado = sorted(diccionario_ips.items(), key=lambda x: x[1], reverse=True)

    
    for ip, cantidad in ordenado:
        print(f"{ip}: {cantidad} veces")
        
        
def ip_mas_repetida(diccionario_ips):
   
    if not diccionario_ips:
        return []

   
    max_valor = max(diccionario_ips.values())

    # Devuelve todas las IPs cuya cantidad coincide con la mayor cantidad.
    return [ip for ip, cant in diccionario_ips.items() if cant == max_valor]

if __name__ == "__main__":
    # Caso de prueba: incluye IPs repetidas, un empate, límites permitidos,
    # espacios, partes faltantes o sobrantes, letras y valores fuera de rango.
    ips = [
        "192.168.1.10", "10.0.0.5", "192.168.1.10", "45.170.23.11",
        "10.0.0.5", "192.168.1.10", "45.170.23.11", "45.170.23.11",
        "8.8.8.8", "45.170.23.11", " 8.8.8.8 ",
        "0.0.0.0", "0.0.0.0", "255.255.255.255",
        "192.168.1", "192.168.1.1.1", "192.168.one.1",
        "256.168.1.1", "192.168.1.256", "-1.168.1.1",
        "192..1.1", "",
    ]

    
    diccionario_ips = cantidad_apariciones(ips)

   
    mostrar_resultado(diccionario_ips)

   
    top = ip_mas_repetida(diccionario_ips)

    print(f"\nIP(s) más repetida(s): {', '.join(top)}")



