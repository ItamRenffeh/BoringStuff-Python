my_pets = ["karen", "juan" , "pedro" , "julio"]

name = input("Chequea si es tu mascota> ")

if name not in my_pets:
    print(name + " No pertenece a tus mascotas")
else : print("Tu mascota es " + name)
