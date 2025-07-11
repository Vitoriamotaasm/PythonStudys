#add - adiciona itens
setExemploNumeros = set()
setExemploNumeros.add(1)
setExemploNumeros.add(2)
setExemploNumeros.add(3)
setExemploNumeros.add(4)
setExemploNumeros.add(5)
setExemploNumeros.add("Amanda")
print(setExemploNumeros)

setLetras = {"A", "B", "C"}
print(setLetras)

#union - unir sets
set1 = {"Allan", "Berenice", "Roger"}
set2 = {39, 21, 45}
uniaoSets = set1.union(set2)
print(uniaoSets)

#intersetion - intens em comum
listaSet1 = {"Python", "C++", "Java"}
listaSet2 = {"VisualG", "Logica", "Python"}
imprimindo = listaSet1.union(listaSet2)
print(imprimindo)

valorEmAmbos = listaSet1.intersection(listaSet2)
print(valorEmAmbos)

#symmetric_difference_update: itens diferentes
listaSet1.symmetric_difference_update(listaSet2)
print(listaSet1)

#symmetri_difference: itens diferentes em ambos conjuntos
listaS1 = {"Python", "C++", "Java"}
listaS2 = {"VisualG", "Logica", "Python"}
naoEstaoEmAmbas = listaS1.symmetric_difference(listaS2)
print(naoEstaoEmAmbas)

#Sets nao aceitam valores repetidos
setNumero = {1, 2, 3, 4, 5, 6, 6, 7, 8}
print(setNumero)
print(len(setNumero))

setExemplo1 = {"A", "B", "C"}
setExemplo2 = {1, 2, 3}
setExemplo3 = {True, False, True}
setExemplo4 = {"Maca", 12, True}
setExemplo2.update(setExemplo1) #unindo os sets
print(setExemplo1)
print(setExemplo2)
print(setExemplo3)
print(setExemplo4)

#imprimindo sets com for
listaObjetos = {"Casa", "Moto", "Bicicleta", "Lancha"}
for i in listaObjetos:
    print(i)
#add item no set
listaObjetos.add("Carro")
print(listaObjetos)
#removendo item no set
listaObjetos.remove("Moto")
print(listaObjetos)
#removendo o ultimo item do set
listaObjetos.pop()
print(listaObjetos)
#verificar se existe um item no set
print("Bicicleta" in listaObjetos)