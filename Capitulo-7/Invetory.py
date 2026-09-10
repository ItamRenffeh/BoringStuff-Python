
import pprint

stuff = {"rope": 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
def display_inventario(inventario): 
    print("Invetario: ")
    total_stuff = 0
    for k, v in inventario.items():
        total_stuff = total_stuff + v
        print ( str(k) + ": " + str(v))
    print("Total: " + str(total_stuff))
    
display_inventario(stuff)

# Versión original:
# def add_inventory(inventario, nuevos):
#     for i in range(len(nuevos)):
#         if nuevos[i] in inventario:
#             inventario[nuevos[i]] += 1
#         else:
#             inventario[nuevos[i]] = 1
#Version compacta Por copilot:
def add_inventory(inventario, nuevos):
    for item in nuevos:
        inventario[item] = inventario.get(item, 0) + 1

add_inventory(stuff, dragon_loot)

pprint.pprint(stuff)