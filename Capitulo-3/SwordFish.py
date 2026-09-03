name = ""
password = ""

while True:
    print("Write your name, please")
    name = input(">")
    if name == "matias":
        print("Ingrese la contraseña, pista:Un pescado")
        password = input(">")
        if password == "swordfish":
            break
        else : print("Contraseña incorrecta")
    else : print("Name incorrecto")
print("Acceso aprobado")
    

