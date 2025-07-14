cadastroUsuarios = {
    "usuario1": {"nome": "Amanda", "idade": 25, "email": "amanda@email.com"},
    "usuario2": {"nome": "Carlos", "idade": 31, "email": "carlos@email.com"},
    "usuario3": {"nome": "Bruna", "idade": 19, "email": "bruna@email.com"}
}

print(cadastroUsuarios["usuario2"])

#Atualizando dados 
cadastroUsuarios["usuario3"] ["email"] = "nova_bruna@email.com"
print(cadastroUsuarios)

#Adicionando um usuario
cadastroUsuarios["usuario4"] = {"nome": "Luana", "idade": 22, "email": "luana@email.com"}
print(cadastroUsuarios)