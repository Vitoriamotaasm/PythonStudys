lista1 = ["a", "b", "c"]
lista2 = ["d", "e", "f"]

lista1.extend(lista2) #extend une duas listas
print(lista1)
lista1.remove("e") #removendo pelo valor

lista1.pop(2) #remove por posicao
print(lista1)

lista1.pop() #removendo o ultimo elemento da lista
print(lista1)

del lista1[0] #remove por indice
print(lista1)

lista1.clear() #remove tudo
print(lista1)

lista1.append("Maca") #add item no final
print(lista1)

lista1.insert(1, "Goiaba") #add item em posicao especifica 
print(lista1)

if "Goiaba" in lista1:
    print("Sim, a fruta goiaba existe na lista")
else:
    print("Nao encontramos a fruta")

lista1[2] = "Banana"
print(lista1)

lista1[1:3] = ["A", "B"] #alteracao em fatia (slice): troca um pedaco da lista por outra coisa
print(lista1)