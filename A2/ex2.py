list_num = [2, 7, 4, 5, 1, 8, 3, 9, 6, 10]

numR = int(input("Introdueix un número per buscar a la llista: "))
contador = 0

for num in list_num:
    if num == numR:
        contador += 1

print(f"{numR} apareix {contador} vegades a la llista.")
