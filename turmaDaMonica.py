turma = []
print(turma)

turma.append("Mônica")
turma.append("Magali")
turma.append("Chico Bento")
print(turma)

# Digite o nome do cebolinha e do cascão
for i in range(2):
    turma.append(input("Digite um nome: "))
print(turma)

del turma[-1]
del turma[-1]
print(turma)

turma.insert(0,"Sansão")
print(turma)
print("Essa turma tem",len(turma),"membros")
