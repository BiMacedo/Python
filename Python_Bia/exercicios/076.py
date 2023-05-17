valores =[]
for cont in range(0,4):
    valores.append(int(input('Digite um valor: ')))

#valores.append('5')
#valores.append('7')
#valores.append('18')

for c, v in enumerate(valores):
    print(f'na posição {c} encontrei {v}')
print('ufa!')

a = [1,2]
# [: cria uma cópia   ]
b= a[:]

b[2]=8

print()