aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))

if aluno['media'] >= 7:
    aluno['situação']= 'aprovado'
elif 5<= aluno ['media'] < 7:
    aluno['situação']='recuperação'
else: 
    aluno['situação']='reprovado'

print(aluno)