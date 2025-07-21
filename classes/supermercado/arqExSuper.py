import supermercado as sp

sp.Supermercado()

print(sp.produtos["Arroz"])


from supermercado import produtos

print(produtos["Feijao"])

#Imprimindo o nome de todos os produtos
for i in produtos:
    print(i)

#Imprimindo o preço de todos os produtos
for i in produtos:
    print(produtos[i])

#Imprimindo produto e preco
for produtos, preco in produtos.items():
    print(produtos, "-", preco)


from supermercado import departamento

for produto, preco in departamento.items():
    print(produto)
    for produto, preco in preco.items():
        print("Produto:", produto, "R$", preco)