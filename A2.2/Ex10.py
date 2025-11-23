# Diccionari d'alumnes amb informació interna
alumnes = {
    'Marta': {'edat': 18, 'nota_final': 8.5},
    'Joan': {'edat': 19, 'nota_final': 6.7},
    'Anna': {'edat': 18, 'nota_final': 9.2}
}

# Inicialitzar variables per guardar el millor alumne
millor_nom = None
millor_nota = -1  # Comencem amb una nota impossible per assegurar la comparació

# Iterar sobre el diccionari
for alumne, info in alumnes.items():
    if info['nota_final'] > millor_nota:
        millor_nota = info['nota_final']
        millor_nom = alumne

# Mostrar el resultat
print(f"L'alumne amb millor nota és {millor_nom} amb {millor_nota}")
