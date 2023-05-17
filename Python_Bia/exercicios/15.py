import math
 
salHora = float(input('Digite seu salario hora: '))
HorasTra = int(input('Digite as horas trabalhadas no mês: '))
tx_ir = 0.11
tx_inss = 0.08


Bruto = salHora*HorasTra
INSS  = (Bruto*tx_inss)
ir = Bruto*tx_ir
sind = Bruto*0.03
descontos = INSS+ir+sind
Salario_Liquido = Bruto - descontos


print(f'Salario Bruto: R${Bruto:.2f}')
print(f'INSS: R${INSS:.2f}')
print(f'Imposto de Renda: R${ir:.2f}')
print(f'Sindicato: R${sind:.2f}')
print(f'Salario Liquido é: R${round(Salario_Liquido)}')

