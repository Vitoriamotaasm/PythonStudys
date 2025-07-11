listaMinMax = [52, 10, 20, 100, 50, 300, 5]
print(min(listaMinMax))
print(max(listaMinMax))

listaNumeros1ate10 = [i for i in range(101) if i <= 10]
print(listaNumeros1ate10)

listaDoisEmDois = list(range(0,100,2))
print(listaDoisEmDois)

listaOriginal = ["Carro", "Moto", "Bicicleta", "Lancha"]
listaCopiada = listaOriginal.copy() #copiando a lista
print(listaCopiada)

lista1Letras = ["A", "B", "C"]
lista2Numeros = [1, 2, 3]
listaJoin = lista1Letras + lista2Numeros #unindo listas
print(listaJoin)

l1 = ["a1", "b1", "c1"]
l2 = [11, 12, 13]
for item in l2:
    l1.append(item) #append inclui no final
print(l1)
