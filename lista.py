lista1 = [1]
lista2 = lista1
lista1[0] = 2
print(lista2)

lista1 = [1]
lista2 = lista1[:]
lista1[0] = 2
print(lista2)

lista = [10,8,6,2,4]
nova_lista = lista[1:3]
print(nova_lista)



lista = [10,8,6,2,4]
nova_lista = lista[1:-1]
print(nova_lista)

lista = [10,8,6,2,4]
nova_lista = lista[-1:1]
print(nova_lista)

lista = [10,8,6,2,4]
nova_lista = lista[:3]
print(nova_lista)

lista = [10,8,6,2,4]
nova_lista = lista[3:]
print(nova_lista)

lista = [10,8,6,2,4]
nova_lista = lista[:]
print(nova_lista)

lista = [10,8,6,2,4]
del lista[1:3]
print(lista)

lista = [10,8,6,2,4]
del lista[:]
print(lista)