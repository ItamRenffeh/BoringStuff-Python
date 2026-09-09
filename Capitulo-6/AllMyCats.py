cat_names = []
i = 0
 
while True:
    print("Introduzca el nombre de su gato" + str(len(cat_names)+1) + "O aprete ENTER para finalizar")
    name = input(">")
    
    if name == "": break
    
    cat_names = cat_names + [name]
    
print("Los nombres de los gatos son:")
for name in cat_names:
    i = i + 1
    print("" + str(i) + " "+ name)
