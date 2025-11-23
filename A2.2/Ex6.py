preus1 = {'pa': 1.2, 'llet': 0.9}
preus2 = {'formatge': 2.5, 'pa': 1.1}
preus_fusionats = preus1 | preus2
preus_fusionats = preus1.copy()  # Copiamos preus1
preus_fusionats.update(preus2)   # Actualizamos con preus2 (sobrescribe valores)
print(preus_fusionats)