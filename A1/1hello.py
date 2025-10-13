print("Hola, món!")
n1 = int(input("Introdueix un nombre: "))
n2 = int(input("Introdueix un altre nombre: "))
print("La suma és:", n1 + n2)
ps = int (input("Introdueix un nombre per saber si és parell o senar: "))
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
for l in range (1, 11):
    print(f"{x} * {l} = {x * l}")

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
textdna ="dajdnakdj"
print(len(textdna))
text = "Hello world".upper()
print(text)
