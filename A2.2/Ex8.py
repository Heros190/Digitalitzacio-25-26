# Diccionari amb productes i preus
preus = {'motxilla': 45, 'llapis': 1, 'calculadora': 25, 'carpeta': 15}

# Crear un nou diccionari amb productes que costin més de 20 €
preus_filtrats = {producte: preu for producte, preu in preus.items() if preu > 20}

# Mostrar el diccionari filtrat
print(preus_filtrats)