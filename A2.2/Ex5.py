paraula = input("Introdueix una paraula: ")
comptador = {}  # Diccionari buit

for lletra in paraula:
    if lletra in comptador:
        comptador[lletra] += 1  # Si ja existeix, sumem 1
    else:
        comptador[lletra] = 1   # Si no existeix, iniciem a 1
print(comptador)