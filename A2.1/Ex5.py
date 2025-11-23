list_num = [2, 7, 4, 2, 1, 6, 3, 7, 6, 10]

llista_sense_dups = []

for num in list_num:
    if num in llista_sense_dups:
        llista_sense_dups.remove(num)
    llista_sense_dups.append(num)
    
#for num in list_num:
#   if num not in llista_sense_dups:
#        llista_sense_dups.append(num)

print("Llista original:", list_num)
print("Llista sense duplicats:", llista_sense_dups)
