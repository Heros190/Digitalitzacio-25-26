# Diccionari amb alumnes i les seves notes
notes = {
    'Anna': [8, 9, 7],
    'Pau': [5, 6, 6],
    'Laura': [10, 9, 8]
}

# Iterar sobre cada alumne
for alumne, llistanotes in notes.items():
    mitjana = sum(llistanotes) / len(llistanotes)  # Calcular la mitjana
    print(f"{alumne} → {mitjana:.2f}")  # Mostrar amb 2 decimals