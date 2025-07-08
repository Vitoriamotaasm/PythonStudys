#comentario simples

"""
comentario longo 
"""

#variaveis
nome = "Ana Paula"
print(nome)

idade = 25
print(idade)

#pra criar duas variaveis na mesma linha
nomeUsuario = "Amanda"; sobreNomeUsuario = "Souza"
print(nomeUsuario + sobreNomeUsuario) #isso concatena, ou seja, junta.
print(nomeUsuario, sobreNomeUsuario) #isso vai imprimir normal

#combinando texto fixo com variaveis
print("Nome:", nomeUsuario)
print("Sobrenome:", sobreNomeUsuario)

#a forma real usada em empresas é assim:
print(f"Nome: {nomeUsuario}")
print(f"Sobrenome: {sobreNomeUsuario}")
#O f antes das aspas quer dizer que a string vai ter variaveis dentro.
#O que coloca dentro das {} ele troca pelo valor da variavel

#Refazendo o codigo: 
nomeUsuario = "Amanda"
sobreNomeUsuario = "Souza"

print(f"Nome completo: {nomeUsuario} {sobreNomeUsuario}")