#Argumentos com chaves
def provaAluno(nota1, nota2, nota3):
    print("O aluno tirou:", nota3)
provaAluno(nota1 = 9, nota2 = 7, nota3 = 10)

#Funcao com um parametro padrao

def funcaoNome(nome = "Python"):
    print("Meu nome é", nome)

funcaoNome("Alice")
funcaoNome("Pedro")
funcaoNome()
funcaoNome("Carolina")

def funcaoListaNumeros(numero):
    print(numero)
    for item in numero:
        print(item)

listaNumeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

funcaoListaNumeros(listaNumeros)

#funcao pra multiplicar
def multiplicacaoDoisNumeros(numeroRecebido):
    return 10 * numeroRecebido 
print(multiplicacaoDoisNumeros(5))
print(10, "x", 10, "=", multiplicacaoDoisNumeros(10))
