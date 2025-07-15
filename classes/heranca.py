class alunoEscolaPai:
    #construtor
    def __init__(self, nome, sexo, media, situacao):
        self.nome = nome
        self.sexo = sexo
        self.media = media
        self.situacao = situacao

    def imprimirDados(self):
        print("Estudante:", self.nome)
        print("Sexo:", self.sexo)
        print("Média:", self.media)
        print("Situação:", self.situacao)

#para herdar os dados, basta colocar o nome na classe que quer herdar entre os parenteses.
class alunoEscolaFilho(alunoEscolaPai):
    #quando eu crio um construtor na classe filho, esse construtor sobrescreve o da classe pai
    def __init__(self, nome, sexo, n1, n2, n3, n4):
        self.media = (n1 + n2 + n3 + n4) / 4
    
        if self.media >= 6:
            self.situacao = "aprovado(a)"
        else: 
            self.situacao = "Reprovado(a)"

#com a funcao super chamamos o construtor da classe pai. O init é o construtor da classe pai
        super().__init__(nome, sexo, self.media, self.situacao)

aluno1 = alunoEscolaFilho("Pedro", "M", 9, 8, 10, 10)

aluno1.imprimirDados()
 