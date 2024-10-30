lista = [8,10,6,2,4]
troca = True

while troca:
    troca = False
    for i in range(len(lista)-1):
        if lista[i] > lista[i+1]:
            troca = True
            lista[i],lista[i+1] = lista[i+1],lista[i]
print(lista)

lista2 = [8,10,6,2,4]
lista2.sort()
print(lista2)

lista2.reverse()
print(lista2)

x = sorted(lista2,reverse=True)
print(x)
