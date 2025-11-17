list_num = [2, 7, 4, 5, 1, 8, 3, 9, 6, 10]

maxim = list_num[0]
minim = list_num[0]

for num in list_num:
    if num > maxim:
        maxim = num
    if num < minim:
        minim = num

print("Valor màxim:", maxim)
print("Valor mínim:", minim)
# maxim = max(list_num)
# minim = min(list_num)