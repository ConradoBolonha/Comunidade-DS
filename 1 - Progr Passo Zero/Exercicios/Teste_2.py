print()
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite um segundo valor: '))
n3 = int(input('Digite um trerceiro valor: '))
n4 = int(input('Digite um quarto valor: '))

if n1 > n2 > n3 > n4:
    print(f'{n1}')
    if n2 > n1 > n3 > n4:
        print(f'{n2}')
    if n3 > n1 > n2 > n4:
        print(f'{n3}')
    else:
        print(n4)
print()
