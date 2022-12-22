list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
list_ap = []

for cont in list_1:
    if cont % 2 != 0:
        list_ap.append(cont)
print(f'Os números são {list_ap}')
