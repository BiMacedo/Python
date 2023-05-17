ano = int(input("Ano de nascimento: "))
AnoAtual = 2023
idade = (AnoAtual-ano)

if idade<18:
    print('Ainda vai se alistar!')
elif idade ==18:
    print('Está na hora de se alistar!')
else: idade>=19
print('Passou da hora de se alistar!')

print('Se tem {}'.format(idade))
