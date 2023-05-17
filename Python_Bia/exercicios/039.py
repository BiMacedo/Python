from datetime import date

atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc


if idade <9: 
    print('Sua idade é {} anos'.format(idade))
    print('Mirim.')
elif idade >9 and idade <14: 
    print('Sua idade é {} anos'.format(idade))
    print('Infantil.')
elif idade >14 and idade <19:
    print('Sua idade é {} anos'.format(idade))
    print('Junior')
elif idade == 20:
    print('Sua idade é {} anos'.format(idade))
    print('SêNIOR')
elif idade >20:
    print('Sua idade é {} anos'.format(idade))
    print('Master')

