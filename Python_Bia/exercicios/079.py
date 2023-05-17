lista = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in list:
        list.append(n)
    else:
        print('valor duplicado')
    r = str(input('Digite um valor: '))
    if r in 'Nn':
        break
