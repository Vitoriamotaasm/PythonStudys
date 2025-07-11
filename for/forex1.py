#for = para

letras = ["A", "B", "C", "D", "E"]
for posicao in letras:
    print("Letra: ", posicao)

for i, letras in enumerate(letras):
    print(i, letras)

for i in "Python":
    print(i)

listaCores = ["amarelo", "vermelho", "laranja", "rosa"]
for i in listaCores:
    if i == "laranja":
        print("Cor laranja encontrada com sucesso!")
        break

