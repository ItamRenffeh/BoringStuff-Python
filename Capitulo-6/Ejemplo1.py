def lista_con_and(lista):
    if len(lista) == 0:
        return "La lista se encuentra vacia"
    if len(lista) == 1:
        return str(lista[0])
    if len(lista) == 2:
        return str(lista[0]) + " and " + str(lista[1])

    texto = ""
    for i in range(len(lista)):
        if i == len(lista) - 1:
            texto += "and " + str(lista[i])
        else:
            texto += str(lista[i]) + ", "
    return texto


spam = ['apples', 'bananas', 'tofu', 'cats']
print(lista_con_and(spam))
print(lista_con_and([]))
print(lista_con_and(['solo']))
print(lista_con_and(['a', 'b']))