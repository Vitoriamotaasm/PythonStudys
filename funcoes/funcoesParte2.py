def funcaoDivisao(numero1, numero2):
    return numero1 / numero2

resultado = funcaoDivisao(10, 2)
print(resultado)


def funcaoMedia(nota1, nota2, nota3, nota4):
    return(nota1 + nota2 + nota3 + nota4) / 4
media = funcaoMedia(10, 6, 8, 10)
print(media)

#funcao com args
def frutaPreferida(*args):
    print("Eu gosto de ", args[2])

frutaPreferida("Banana", "Goiaba", "Laranja", "Kiwi")

def unirListas(*listas):
    print(listas)

lista1 = [1, 2, 3, 4, 5]
lista2 = [6, 7, 8, 9, 10]

unirListas(*lista1, *lista2)

#se o numero de argumentos for desconhecido, adicionamos a ** antes do nome do parametro.
def funcaoKwargs(**parametro):
    print("Eu moro em", parametro["cidade1"])

funcaoKwargs(cidade1 = "Sao Paulo", cidade2 = "Rio de Janeiro")