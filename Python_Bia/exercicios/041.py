list = []

for i in range(0,4):
    list.append(int(input(f'Digite a nota {i}: ')))
    soma = sum(list)
    quant=len(list)
    media = soma/quant
    print(f'As notas são: {list} e a média é {media}')
if media >6:
    print('Aprovado')
elif media < 5.9: 
    print('Reprovado')