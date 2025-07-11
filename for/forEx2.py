listaNomes = ["Bia", "Raquel", "Allan", "Mafalda"]

for i in listaNomes:
    if i == "Allan":
        continue
    print(i)

for i in range(10): #range(start, stop e step) = range(start = 1)
    print(i)

#contar de 1 ate 10 com range
#range(start = 1, stop = 10, step = 1)
for i in range(1, 11, 1):
    print("Numero: ", i)

#contar do 20 ate o 10
for i in range(20, 9, -1):
    print("Posição: ", i)