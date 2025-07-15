# ao inves do self podemos usar o mysillobject
class informcacoesAluno:
    def __init__(mysillyobject, nomeAluno, idadeAluno, mediaAluno):
        mysillyobject.nome = nomeAluno
        mysillyobject.idade = idadeAluno
        mysillyobject.media = mediaAluno
    
    def funcaoImprimirDadados(mysillyobject):
        print("Nome:", mysillyobject.nome)
        print("Idade:", mysillyobject.idade)
        print("Média:", mysillyobject.media)

pegaInformacoes = informcacoesAluno("Pedro", 18, 9)
pegaInformacoes.funcaoImprimirDadados()


class notaAluno:
    def __init__(self, nota1, nota2, nota3, nota4):
        self.n1 = nota1
        self.n2 = nota2
        self.n3 = nota3
        self.n4 = nota4

notas = notaAluno(9, 8, 7, 10)

print("Nota3:", notas.n3)

#alterando o objeto da classe
notas.n3 = 10
print("Nota3:", notas.n3)