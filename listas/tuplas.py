#Tuplas nao sao alteraveis

tuplaLetras = ("A", "B", "C", "D")
print(tuplaLetras)
print(type(tuplaLetras)) #imprimindo o tipo da tupla
print(len(tuplaLetras)) #tamanho da tupla
print(tuplaLetras[1])

novaLetra = ("E", )
print(novaLetra)
print(type(novaLetra))

#Cria nova tupla
tuplaLetras += novaLetra
print(tuplaLetras)

tuplaNumeros = (1, 2, 3, 4, 5, 6, 7)
listaNumeros = list(tuplaNumeros) #convertendo tupla em lista
listaNumeros.remove(4)
tuplaNumeros = tuple(listaNumeros) #convertendo a lista em tupla
print(tuplaNumeros)
