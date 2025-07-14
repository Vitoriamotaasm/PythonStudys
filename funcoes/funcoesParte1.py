#recebe o parametro e imprime o resultado na tela
print("Exemplo 1 de função")


#uma funcao
def minhaPrimeiraFuncao():
    print("Essa é a minha primeira função criada com Python")

minhaPrimeiraFuncao()


def funcaoTexto(nome):
    print(nome, "Santos")

funcaoTexto("Ana")
funcaoTexto("Roger")
funcaoTexto("Marcos")


def funcaoSaudacao(saudacao, nome):
    print(saudacao, nome)

funcaoSaudacao("Boa noite", "Ana")
funcaoSaudacao("Bom dia", "Cesar")
funcaoSaudacao("Boa tarde", "Luisa")


#funcao com dois parametros
def funcaoComArgumentos(nome, sobrenome):
    print("Nome completo:", nome, sobrenome)

nomeInput = input("Digite o seu nome: ")
sobrenomeInput = input("Digite o seu sobrenome: ")

funcaoComArgumentos(nomeInput, sobrenomeInput)
