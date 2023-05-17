num =  int(input('Digite um numero inteiro: '))
print('''Escolha uma das bases para conversão: 
[1] Binario
[2] Octal 
[3] Hexadecimal
''')

opção = int(input('Sua opção: '))

if opção == 1:
    print('{} convertido para binario é {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print('{} convertido em octal é {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('{} convertido em hexadecimal é {}'.format(num, hex(num)[2:]))
else:
    print('Opção Inválida')
