dicionario = {
    "Ana": 21,
    "Marcela": 34,
    "Pedro": 42
}

print(dicionario)
print(len(dicionario)) 
print(type(dicionario))

dicionario2 = dicionario.copy()
print("Exemlo dicionario2:", dicionario2)

dicionario3 = dict(dicionario)
print("Exemplo dicionario 3:", dicionario3)


dicionarioPessoas = {
    "Ana": 21,
    "Marcela": 34,
    "Pedro": 42,
    "Pedro": 53
}

print(dicionarioPessoas)

#Pegar a idade da Marcela
dados = dicionarioPessoas["Marcela"]
dados2 = dicionarioPessoas.get("Pedro")
print(dados)
print(dados2)

#Pegar somente os nomes (coluna 1)
nomes = dicionarioPessoas.keys()
print(nomes)

#Pegar somente as idades (coluna 2)
idades = dicionarioPessoas.values()
print(idades)


alimentos = {
    "arroz": 35.90,
    "macarrao": 21.90,
    "feijao": 29
}

print(alimentos)

#Alterando o preco do macarrao
alimentos["macarrao"] = 39.90
print(alimentos)

#Alterando o preco do feijao
alimentos.update({"feijao": 31})
print(alimentos)

#Adicionando item no dicionario
alimentos ["salsicha"] = 35
print(alimentos)

#Pop remove o item do dicionario
alimentos.pop("salsicha")
print(alimentos)

#remove o ultimo item do dicionario
alimentos.popitem()
print(alimentos)

#Remove todos os itens de uma vez
alimentos.clear()
print(alimentos)

#adicionando os itens
alimentos["arroz"] = 35.90
alimentos["macarrao"] = 21.90
alimentos["feijao"] = 29
print(alimentos)

#Deletando o arroz 
del alimentos["arroz"]
print(alimentos)

#procurando o alimento
if "macarrao" in alimentos:
    print("Alimento encontrado com sucesso!")
else: 
    print("Alimento nao encontrado na lista")

letras = {
    "Letra 1" : "A",
    "Letra 2" : "B",
    "Letra 3" : "C",
    "Letra 4" : "D",
    "Letra 5" : "E",
    "Letra 6" : "F"
}
print(letras)

#imprimindo os titulos
for i in letras:
    print(i)

#imprimindo os valores
for i in letras:
    print(letras[i])

#imprimindo os valores exemplo 2
for i in letras.values():
    print(i)

#imprimindo tudo
for i, valor in letras.items():
    print(i, "-", valor)

exemplo1 = {
    "A" : 1,
    "B" : 2
}
exemplo2 = {
    "C" : 3,
    "D" : 4
}
exemplo3 = {
    "E" : 5,
    "F" : 6
}

unirDicionarios = {
    "Dicionario 1:" : exemplo1, 
    "Dicionario 2:" : exemplo2, 
    "Dicionario 3:" : exemplo3
}
print(unirDicionarios)

escola = {
    "Turma 1" : {
        "Andre:" : 10,
        "Amanda:" : 8
    },
    "Turma 2" : {
        "Cesar:" : 6,
        "Alessandra:" : 7
    },
    "Turma 3" : {
        "Roger" : 9,
        "Rosiane" : 10
    }
}
for tur1, tur2 in escola.items():
    print(tur1)
    for tur1, tur2 in tur2.items():
        print("Aluno:", tur1, "- Nota:", tur2)