
z = int (input("Introdueix un nombre: "))
v = int (input("Introdueix un altre nombre: "))
b = int (input("Introdueix un tercer nombre: "))
if z >= v and z >= b:
    print(f"El nombre més gran és: {z}")
elif v >= z and v >= b:
    print(f"El nombre més gran és: {v}")
else:
    print(f"El nombre més gran és: {b}")