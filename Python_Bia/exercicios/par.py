list = []
pares = []
impares = []

for i in range (0,10):
    int(input(f'Digite um numero: '))
    if i % 2== 0:
       pares.append(i)
    else: 
      impares.append(i)   

    print(f'Pares {pares}')
    print(f'impares {impares}')