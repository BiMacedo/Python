salario = float(input('Digite seu salario: '))

if salario <2000.00:
    print('Isento.')
elif salario > 2000.01 and salario <=3000.00:
    salario = salario - 2000
    imp = (salario * 0.08)
    print('Seu imposto é {}'.format(imp))
elif salario > 3000.01 and salario < 4500.00:
    salario = salario - 3000
    imp = (salario * 0.18)+80
    print('Seu imposto é {}'.format(imp))
elif salario > 4500.00:
    salario = salario - 4500
    imp = (salario * 0.28)+350
    print('Seu imposto é {}'.format(imp))

