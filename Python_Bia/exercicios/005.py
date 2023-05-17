vel = int(input('Digite sua velocidade: '))


if vel > 80:
    print('Você foi MULTADO!!!')
    multa = (vel-80) * 7
    print('Voce deve pagar de multa R${:.2f}'.format(multa))
else:
    print('Tenha uma Belo dia!!!')