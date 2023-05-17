numeros = ('zero', 'um', 'dois', 'tres','quatro','cinco','seis'
           'sete', 'oito', 'nove', 'dez')

while True: 
    num = int(input('Digite um numero: '))
    if 0 <= num <= 10:
        break
        print('Tente novamente ', end='')

print(f'Voce digitou o numero {numeros[num]}')
#for pos, num in enumerate(numeros):
  #  print(f'escolha um numero {numeros} na posição {pos}')
