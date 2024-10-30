lista = [0,3,12,8,2]

print(5 in lista)
print(5 not in lista)
print(12 in lista)

lista = [7,3,11,5,1,9,7,15,13]
maior = lista[0]

for i in range(1    ,len(lista)):
    if lista[i] > maior:
        maior = lista[i]
print(maior)
print(max(lista))