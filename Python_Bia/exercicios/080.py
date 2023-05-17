list = []

for c in range(0,5):
    n = int(input('Digite um numero: '))
    if c == 0 or n > list[-1]:
        list.append(n)
        print('Adicionado')
    else: 
        pos = 0
        while pos < len(list):
            if n <= list[pos]:
                list.insert(pos, n)
                print(list)
                break
            pos +=1
print(list)