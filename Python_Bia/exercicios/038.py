from datetime import date 

atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual-nasc
print('Quem nasceu em {} tem {} em {}'.format(nasc,idade, atual))

if idade < 18:
    saldo = 18 - idade
    ano = atual + saldo
    print('Seu alistamento será em {}'.format(ano))
    print('ainda vai se alistar. Falta {} para se alistar.'.format(saldo))
elif idade == 18:
    print('Hora de se alisatr.')
elif idade > 18:
    saldo = idade - 18
    ano = atual -saldo
    print('Voce se alistou em {}'.format(ano))
    print('Passou do tempo. Já se passou {} anos.'.format(saldo))

