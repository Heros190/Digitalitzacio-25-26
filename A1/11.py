s = "Hello"
lletra = "e"
cont= 0
for x in s:
    if x == lletra:
        cont += 1
print(f"La lletra '{lletra}' apareix {cont} vegades a la paraula '{s}'")

sinvertida = s[::-1]
print(sinvertida)