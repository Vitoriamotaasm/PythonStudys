linha = 0
while linha < 3:
    coluna = 0
    while coluna < 3:
        print("Linha:", linha, " - Coluna", coluna)
        coluna += 1
    linha += 1

numeroInicial = 1
numeroFinal = int(input("Digite um numero maior que 1: "))

while numeroInicial <= numeroFinal:
    print("Escolhi: ", numeroInicial)
    numeroInicial += 1

numero = 1
numeroPar = int(input("Digite um numero maior que 1: "))
while numero <= numeroPar:
    if numero % 2 == 0:
        print(numero, " ")
    numero += 1