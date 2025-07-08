nota1 = nota2 = nota3 = nota4 = media = 0
aluno = "Maria Pichula"

print(aluno)

nota1 = 9
print(nota1)
nota2 = 10
print(nota2)
nota3 = 8
print(nota3)
nota4 = 5
print(nota4)

media = (nota1 + nota2 + nota3 + nota4) /4
print(media)


#com inputs
aluno = input("Digite o nome do aluno: ")

nota1 = input("Digite a nota 1: ")
nota2 = input("Digite a nota 2: ")
nota3 = input("Digite a nota 3: ")
nota4 = input("Digite a nota 4: ")

media = (float(nota1) + float(nota2) + float(nota3) + float(nota4)) /4
print("Aluno: " + aluno)
print("Média:",media)

#utilizando clean code:
aluno = input("Digite o nome do aluno: ")

nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))
nota3 = float(input("Digite a nota 3: "))
nota4 = float(input("Digite a nota 4: "))

media = (nota1 + nota2 + nota3 + nota4) / 4

print(f"Aluno: {aluno}")
print(f"Média: {media}")
