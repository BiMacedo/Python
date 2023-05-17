teste = list()
teste.append('Gustavo')

teste.append(40)

galera = list()
galera.append(teste[:])
teste[0] = 'Maria '
teste[1] = 22
galera.append(teste[:])
print(galera)

for p in galera:
    print(p[0])
galera = list()
dado = list()

for c in range(0,3):
    dado.append(str(input('Digite seu nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

print(galera)
totmai = totmen = 0
for p in galera:
    if p[1]>= 21:
        print(f'{p[0]} é maior de idade.')
        totmai+=1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen +=1
print(f'Temos {totmai} e {totmen}')

