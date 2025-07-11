listaFrutas = ["maçã", "banana", "manga", "abacate", "laranja"]
print(listaFrutas)

listaFrutas.append("kiwi")
print(listaFrutas)

listaFrutas.remove("banana")
print(listaFrutas)

if "abacaxi" in listaFrutas:
    print("Abacaxi está na lista")
else: 
    print("Abacaxi não está na lista")

print(len(listaFrutas))

print(listaFrutas[0])
print(listaFrutas[-1])