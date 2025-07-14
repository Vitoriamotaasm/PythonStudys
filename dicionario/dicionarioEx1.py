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