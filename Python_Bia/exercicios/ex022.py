

#ex 022 - Escreva seu nome e transforme em maiusculas, minusculas, a quantidade, e 
nome=str(input('Seu nome? ')).strip()

print('Analisando seu nome...')
print("Seu nome em maiusculas é {}".format(nome.upper()))
print("Seu nome em minusculas é {}".format(nome.lower()))
print('Quantidades de letras no seu nome é {}'.format(len(nome)-nome.count(' ')))
#print('Sue nome tem tantas letras'.format(nome.find(' ')))

separa = nome.split()
print('seu primeiro nome é {}'.format(separa[0],len(separa[0])))

#crie um programa que leia o nome de uma cidade e diga se ela começa ou não com "santo"
#######################################################
nome= str(input('Seu nome? ')).strip()

print('Seu nome tem Silva {}'.format(nome[:6 == 'Silva'] ))

############################################
nome= str(input('Seu nome? ')).strip()

print('Seu nome tem Silva {}'.format('Silva' in nome))



######################################################

nome= str(input('Qual seu nome? '))
if nome == 'Gustavo':
    print('Que nome Lindo!')
else:
   print('Seu nome é normal')
print('Bom dia, {}!'.format(nome))
######################################################

n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite o segundo nota: '))
m = (n1+n2)/2

print('Sua média é: {:1}'.format(m))

if m >=6.0:
    print('Aprovado')
else:
    print('Reprovado')
print('Sua nota é {}'.format(m))






#PDEK920852
################################3