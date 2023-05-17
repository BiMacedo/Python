nome = str(input('Digite seu nome: '))
N1 = float(input("Nota 1: "))
N2 = float(input('Nota 2: '))

media = (N1+N2)/2

if media <5.0:
    print('Reprovado')
elif media >= 5.0 and media <= 6.9:
    print('Recuperação')
else: media >7.0
print('Aprovado')

print('{}, sua média é {}'.format(nome,media))





idade = int(input('Digite sua idade: '))
 
#idade = (2023-idade)

if idade <9: 
    print('Mirim')
elif idade >9 and idade <14: 
    print('Infantil')
elif idade >14 and idade <19:
    print('Junior')
elif idade == 20:
    print('SêNIOR')
elif idade >20:
    print('Master')

#print('Sua idade é {}'.format(idade))





alt = float(input('Altura: '))
peso = float(input('Peso: '))

imc = peso/(alt*alt)

if imc <18.5:
    print('Abaixo do peso')
elif imc >18.5 and imc <25:
    print('Peso ideal') 
elif imc >25 and imc <30:
    print('Sobrepeso')
elif imc >30 and imc <40:
    print('obesidade')
elif imc >40:
    ('Obesidade morbida')