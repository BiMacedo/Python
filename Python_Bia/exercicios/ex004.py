n1 = float(input('Digite a nota: '))
#p1 = float(input('Nota ponderada 1 : '))
n2 = float(input('Digite a nota: '))
#p2 = float(input('Nota ponderada 2: '))
n3 = float(input('Digite a nota: '))
#p3 = float(input('Nota Ponderada 3: '))
n4 = float(input('Digite a nota: '))
#p4 = float(input('Nota ponderada 4: '))

p = 0

while p < 4:
   print(f'Notas ponderadas {p}')
   p +=1

mp = (n1*p1+n2*p2+n3*p3+n4*p4)/(p1+p2+p3+p4)


print('/n Média é {}'.format(mp))

if mp >=7.0:
   print('Aprovado')
elif mp < 5.0:
   print('Reprovado')
elif mp > 5.0 and mp < 6.9:
   print('Recuperação')
   ex = float(input('Nota Exame: '))
   m = (mp+ex)/2
if m> 5.0:
   print('aprovado')
elif m < 4.9:
   print('Reprovado')
print('Média Final: {}'.format(m))
