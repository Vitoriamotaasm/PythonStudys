""""
As classes são as especificaçoes de um ou mais objetos. Ou seja, é um conjunto de objetos / regras.

Objetos - é uma instancia, um item da classe
"""

class minhaPrimeiraClasse:
    idade = 30
    nome = "Joao"

pegaIdade = minhaPrimeiraClasse()
print("Nome:", pegaIdade.nome, "- Idade:", pegaIdade.idade)


class Aluno:
    #propriedade - objetos
    nome = ""
    idade = 0
    altura = 0

#Instanciar o objeto da classe
dados = Aluno()
dados.nome = "Cintia"
dados.idade = 21
dados.altura = 1.69

print("Estudante:", dados.nome)
print("Idade:", dados.idade)
print("Altura:", dados.altura)


class Turma:
    #def é um construtor - metodo construtor.
    #  o metodo construtor em python é o init.
    #self é um parametro da propria class
    def __init__(self, nomeAluno, idadeAluno, alturaAluno):
        self.nome = nomeAluno
        self.idade = idadeAluno
        self.altura = alturaAluno

    def imprimir(self):
        print("Estudante:", self.nome)
        print("Idade:", self.idade)
        print("Altura:", self.altura)

#Instanciar o objeto da classe 
aluno1 = Turma("Pedro", 31, 1.72)
aluno2 = Turma("Rosa", 18, 1.60)
aluno3 = Turma("Alberto", 35, 1.90)

aluno1.imprimir()
aluno2.imprimir()
aluno3.imprimir()