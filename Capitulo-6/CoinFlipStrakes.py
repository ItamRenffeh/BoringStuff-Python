import random

number_of_streaks = 0

for experiment_number in range(10000):
    # Crea una lista con 100 resultados de cara o cruz
    head_or_tail = []
    for i in range(100):
        if random.randint(0, 1) == 0:
            head_or_tail.append("H")
        else:
            head_or_tail.append("T")

    # Revisa si hubo una racha de 6 iguales seguidas
    contador = 0
    for i in range(1, len(head_or_tail)):
        if head_or_tail[i] == head_or_tail[i - 1]:
            contador += 1
        else:
            contador = 0

        if contador == 5:  # 5 porque la cuenta empieza en el segundo elemento
            number_of_streaks += 1
            break

print("Chance of streak: " + str(number_of_streaks / 10000))