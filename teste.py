lst = [1,2,3,4,5]
lst.insert(1,6)
del lst[0]
lst.append(1)

print(lst)

lst2 = [1,2,3,4,5]
lst_2 = []
add = 0

for number in lst2:
    add += number
    lst_2.append(add)

print(lst_2)

lst3 = []
del lst3
print()

lst4 = [1,[2,3],4]
print(lst4[1])
print(len(lst4))

lst5 = ["D","F","A","Z"]
lst5.sort()

print(lst5)

a,b,c = 3,1,2
lst6 = [a,c,b]
lst6.sort()

print(lst6)

a,b,c,d = "A","B","C",""
lst7 = [a,b,c,d]
lst7.reverse()

print(lst7)
