lista1 = ["a", "b", "c"]
lista2 = ["d", "e", "f"]

lista1.extend(lista2) #extend une duas listas
print(lista1)
lista1.remove("e") #removendo letra e da lista

lista1.pop(2) #removendo com o pop o segundo elemento da lista
print(lista1)

lista1.pop() #removendo o ultimo elemento da lista
print(lista1)

del lista1[0] #removendo o primeiro elemento da lista
print(lista1)

lista1.clear() #removendo todos os itens da lista
print(lista1)

lista1.append("Maca") #add itens na lista
print(lista1)

lista1.insert(1, "Goiaba") #add item na 2 posicao
print(lista1)

if "Goiaba" in lista1:
    print("Sim, a fruta goiaba existe na lista")
else:
    print("Nao encontramos a fruta")

lista1[2] = "Banana"
print(lista1)

lista1[1:3] = ["A", "B"]
print(lista1)