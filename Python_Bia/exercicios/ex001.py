# Neste problema, deve-se ler o código de uma peça 1, 
#o número de peças 1, o valor unitário de cada peça 1, 
#o código de uma peça 2, o número de peças 2 
#e o valor unitário de cada peça 2. Após, 
#calcule e mostre o valor a ser pago.

cod = int(input('Código Peça: '))
num = int(input('Número de Peças: '))
vlu = float(input('Valor unitário: '))

cod2 = int(input('Codigo Peça 2: '))
num2 = int(input('Número Peça: '))
vlu2 = float(input('Valor unitario: '))

Total = (num*vlu)
Total2 = (num2*vlu2)

pagar = (Total+Total2)

if pagar>150:
    print('Pagar no crédito')
else:
    print()
    

print('Codigos da peça: {} {}'.format(cod,cod2))

print('Valor a pagar: {}'.format(pagar))
