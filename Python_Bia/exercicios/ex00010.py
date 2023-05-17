list = []

for l in range(0,2):
    list.append(int(input('Digite um numero : ')))
print(list)
if list % 2:
    print(f'Os pares são {list}')
else: 
    print(f'Os impares {list}')
