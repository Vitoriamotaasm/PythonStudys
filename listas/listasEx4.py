listaNome = ["Allan", "Bruna", "Simone", "carla"]
for i in listaNome:
    print(i)

[print(item) for item in listaNome]

contador = 0
while contador < len(listaNome):
    print(listaNome[contador])
    contador = contador + 1

listaNomesC = []
for item in listaNome:
    if "c" in item:
        listaNomesC.append(item)
print(listaNomesC)

listaMaiuscula = [item.upper() for item in listaNome]
print(listaNome)
print(listaMaiuscula)

listaMinuscula = [item.lower() for item in listaNome]
print(listaMinuscula)