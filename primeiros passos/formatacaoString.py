nome = "Maria catarina alves"
print(nome)
print("Total de carcateres: " 
      + str(len(nome)))

print(nome[19])
print(nome[0:6]) #vai pegar do 0 ao 6
print(nome[7:12])
print(nome[13:19])
print(nome[7:])

frase = "Curso de lógica de programação python"

print(frase.upper()) #upper retorna todas as letras em maiuscula
print(frase.lower()) #lower retorna todas as letras em minusculas 

notaProva = "Tirei nota cinco na prova"
print(notaProva.replace("cinco", "dez")) #replace substitui algo do texto

cpf = "123.456.789-10"
cpfPartes = cpf.split(".")

print(cpfPartes)
print(cpfPartes[0])
print(cpfPartes[1])
print(cpfPartes[2])

cpfPartes2 = cpfPartes[2].split("-")
print(cpfPartes2[0])
print(cpfPartes2[1])

print("CPF: " + cpfPartes[0] + cpfPartes[1] + cpfPartes2[0] + cpfPartes2[1])

#----------------------------------

palavraComEspaco = "      Curso de python    "
print(palavraComEspaco)
print(palavraComEspaco.strip()) #remove espaço de uma string

gostoPorFrutas = "Eu gosto de laranja"
print("Laranja" in gostoPorFrutas) #in: está. Ou seja, laranja esta em gosto por frutas.

resultadoProcura = gostoPorFrutas.find("t")
print(resultadoProcura)

copa = "Brasil vai ganhar a copa"
campeao = "Alemanha" not in copa #not in: não está. Ou seja, vai retornar verdadeiro
print(campeao)

aluno = "Rebeca Martins"
nota1 = 9
nota2 = 6
media = (nota1 + nota2) / 2
print("Aluna: " + aluno + " - Média: " + str(media))
print(f"Aluna: {aluno} - Média: {media}")

ajusteTexto = "Aluna: {} - Média: {}"
print(ajusteTexto.format(aluno, media))