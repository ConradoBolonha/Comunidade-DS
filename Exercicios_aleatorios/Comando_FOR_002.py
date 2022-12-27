print('### Rotina trocar pneu ###')

print('Abrir o posta malas')
print('Tirar o estepe')
print('Tirar o macaco')

print('Levantar o carro com o macaco')
for cont in range(10):
    macaco = input(
        'O carro está levando com segurança? s = SIM / n = NÃO: ').lower()
    if macaco == 'n':
        print('Confira o macaco!')
        print('Já conferiu?')
    else:
        print('Pode continuar')
        break

print('Desparafusou as porcas da roda? (s = SIM / 2 = NÃO')
for paraf in range(10):
    parafuso = input('Tirou os parafusos? s = SIM / n = NÃO: ').lower()
    if parafuso == 'n':
        print('Tire os parafusos primeiro!')
        print('Já tirou?')
    else:
        print('Continue tirando o pneu!')
        break

print('Tirar o pneu furado')
print('Colocar o estepe')
print('Parafusar as porcas')
print('Baixar o carro')
print('Colocar o macaco e o estepe furado no porta malas')
print('Fechar o porta malas')
