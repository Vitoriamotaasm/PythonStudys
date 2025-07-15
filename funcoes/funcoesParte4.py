#variavel no escopo global
nome = "Silvana"

def funcao1():
    print(nome)

def funcao2():
    print(nome)

funcao1()
funcao2()

nomeSobrenome = "Steve Jobs"

def funcaoNomeSobrenome():
    print(nomeSobrenome)

def funcaoNomeSobrenome2():
    #escopo local - variavel local
    #quando mudamos o valor da var dentro da funcao n estamos mudando o valor, estamos criando uma nova var, por isso, q a var n é afetada
    nomeSobrenome = "Bill Gates"
    print(nomeSobrenome)

funcaoNomeSobrenome()
funcaoNomeSobrenome2()
print(nomeSobrenome)

idade = 32

def funcaoIdade1():
    print(idade)

def funcaoIdade2():
    #com o global consigo acessar uma var global e alterar valor de uma var global.
    global idade
    idade = 34
    print(idade)

funcaoIdade1()
funcaoIdade2()
print(idade)
