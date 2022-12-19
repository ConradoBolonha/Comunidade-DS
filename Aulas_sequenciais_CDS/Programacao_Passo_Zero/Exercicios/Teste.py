print()
while True:
    num = int(input('Digite um número: '))
    if num < 0:
        break
    for cont in range(1, 11):
        print(f'{num} X {cont + 1} = {num * cont}')
print('Número negativo não permitido!')
print()
