from dadosPessoais import Dados

pessoa1 = Dados("Celso", 34, "Solteiro", 5000 )
pessoa2 = Dados("Beatriz", 41, "Casada", 8000)

Dados.imprimirDados(pessoa1)
Dados.imprimirDados(pessoa2)

#Alterando os dados da pessoa 1
pessoa1.nome = "Sebastian"
pessoa1.idade = 45
pessoa1.estadoCivil = "Casado"
pessoa1.salario = 10.000

Dados.imprimirDados(pessoa1)

#alterando os dados em tempo real
pessoa2.nome = input("Digite o nome: ")
pessoa2.idade = input("Digite a idade: ")
pessoa2.estadoCivil = input("Digite o estado civil: ")
pessoa2.salario = float(input("Digite seu salario: "))

Dados.imprimirDados(pessoa2)