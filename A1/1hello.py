print("Hola, món!")
n1 = int(input("Introdueix un nombre: "))
n2 = int(input("Introdueix un altre nombre: "))
print("La suma és:", n1 + n2)
ps = 7
if ps % 2 == 0:
    print("El nombre és parell")
else:
    print("El nombre és senar")
celsius = float(input("Introdueix la temperatura en Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius} graus Celsius són {fahrenheit} graus Fahrenheit")
base = int(input("Introdueix la base del rectangle: "))
altura = int(input("Introdueix l'altura del rectangle: "))
print ("L'àrea del rectangle és:", base * altura)
x = int(input("Introdueix un nombre: "))
print (f"{x} * 1 = {x * 1}")
print (f"{x} * 2 = {x * 2}")
print (f"{x} * 3 = {x * 3}")
print (f"{x} * 4 = {x * 4}")
print (f"{x} * 5 = {x * 5}")
print (f"{x} * 6 = {x * 6}")
print (f"{x} * 7 = {x * 7}")
print (f"{x} * 8 = {x * 8}")
print (f"{x} * 9 = {x * 9}")
print (f"{x} * 10 = {x * 10}")
paraula = input("Introdueix una paraula: ")
print("La paraula té", len(paraula), "lletres")
a = int(input("Introdueix el nombre fins al que vols arribar: "))
for n in range(1, a+1):
    print(n)
z = int (input("Introdueix un nombre: "))
v = int (input("Introdueix un altre nombre: "))
b = int (input("Introdueix un tercer nombre: "))
if z >= v and z >= b:
    print(f"El nombre més gran és: {z}")
elif v >= z and v >= b:
    print(f"El nombre més gran és: {v}")
else:
    print(f"El nombre més gran és: {b}")
    