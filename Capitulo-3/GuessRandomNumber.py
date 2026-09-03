import random

NumeroSecreto = random.randint(1, 20)
print("Adivina el numero en el que estoy pensado en 1 al 20")

while True:
    NumeroIntento= int(input("Adivina>"))
    if NumeroIntento==NumeroSecreto:
        print("Felicidades adivinaste el numero  " + str(NumeroSecreto))
        break
    elif NumeroIntento>NumeroSecreto:
        print("Te pasaste")
    else: print("Te quedaste corto")

#Tambien se puede realizar con For in range para dar X cantidad de intentos y contarlos