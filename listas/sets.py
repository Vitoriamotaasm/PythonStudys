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