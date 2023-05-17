list = []

for i in range(0,3):
    list.append(int(input(f'Digite um numero {i}: ')))
    par = []
    par = i
    if par / 2:
        print(f'Os pares: {par} ')
    else: 
        print(f'impares: {list}')