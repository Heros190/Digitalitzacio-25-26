# Llista base
list_num = [2, 7, 4, 2, 1, 6, 3, 7, 6, 10]
print("Llista original:", list_num)


# ---------------------------------------------------------

def ordenar_minims(llista):
    temp = llista[:]       # Copiem la llista original
    ordenada = []

    while len(temp) > 0:
        minim = temp[0]

        # Busquem el mínim manualment
        for num in temp:
            if num < minim:
                minim = num

        ordenada.append(minim)
        temp.remove(minim)

    return ordenada


resultado_minims = ordenar_minims(list_num)
print("\nOrdenació trobant mínims successius:")
print(resultado_minims)


# ---------------------------------------------------------

def selection_sort(llista):
    arr = llista[:]   # Copiem per no modificar l'original

    for i in range(len(arr)):
        pos_min = i

        # Buscar el mínim de la part no ordenada
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[pos_min]:
                pos_min = j

        # Intercanviar
        arr[i], arr[pos_min] = arr[pos_min], arr[i]

    return arr


resultado_selection = selection_sort(list_num)
print("\nOrdenació amb Selection Sort:")
print(resultado_selection)


# ---------------------------------------------------------

def insertion_sort(llista):
    arr = llista[:]  # Copiem la llista

    for i in range(1, len(arr)):
        actual = arr[i]
        j = i - 1

        # Moure elements més grans a la dreta
        while j >= 0 and arr[j] > actual:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = actual

    return arr


resultado_insertion = insertion_sort(list_num)
print("\nOrdenació amb Insertion Sort:")
print(resultado_insertion)
