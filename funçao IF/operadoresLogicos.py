"""
Operadores:
and - operador (E)
or - operador (OU)
not - operador (NÃO)
"""

numero1 = 12
numero2 = 21
numero3 = 40
if numero1 > numero2 and numero3 > numero1:
    print("Ambas as condições sao verdadeiras")

nome = "Matheus"
idade = 21
if nome == "Matheus" and idade > 18:
    print("Matheus é maior de idade")

usuario = "Jorge"
senha = 123
if usuario == "Jorge" and senha == 123:
    print("Usuario logado com sucessor!")
else: 
    print("Usuario ou senha inválidos!")

#Operador or
n1 = 10
n2 = 15
n3 = 20
if n1 > n2 or n1 > 5:
    print("Pelo menos uma das condicoes é verdadeiro")

fruta = "Laranja"
if fruta == "Maçã" or fruta == "Laranja":
    print("A fruta é maça ou laranja")

letra = ""
if not letra:
    print("Nao foi encontrado nenhuma letra")

numeroNOT = 0
if not numeroNOT: 
    print("O numero nao pode ser 0 pois 0 é considerado um booleano do tipo false")