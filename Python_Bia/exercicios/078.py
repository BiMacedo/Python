
list = []

mai = 0
men = 0

for c in range(0,5):
    list.append(int(input(f'Digite um numero: {c}:')))
    if c == 0:
        mai == men == list[c]
    else: 
        if list [c] > mai:
            mai = list[c]
        if list[c] < men:
            men = list[c]
print(f'Voce digitou os valores {list}')
print(f'O maior é {mai}')
print(f'o menor é {men}')




#print(sorted(list))
#for t, l in enumerate(list):
 #  print(f'A posição do numero é {t} e o valor {l}')
 
 
 # como mostrar do maior e menor ????
#list = [int(input('Digite um valor na posição 0:')), 
 #       int(input('Digite um valor na posição 1: ')),
  #      int(input('Digite um valor na posição 2: '))]
#print(f'Você digitou {list}')