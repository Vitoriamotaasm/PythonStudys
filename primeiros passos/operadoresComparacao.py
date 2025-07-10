""""
== Igual: verifica se um valor é igual ao outro
!+ Diferente de: Verifica se um valor é diferente do outro
> Maior que: verifica se um valor é maior que outro
>= Maior ou igual: Verifica se um valor ;e maior ou igual a outro
< Menor que: Verifica se um valor é menor que o outro
<= Menor ou igual: Verifica se um valor é menor ou igual a outro
"""

numero1 = float(input("Digite o numero1: "))
numero2 = float(input("Digite o numero 2: "))

if numero1 == numero2:
    print("Ambos os numeros sao iguais")

if numero1 != numero2:
    print("Os numeros sao diferentes")

if numero1 > numero2:
    print("Numero 1 é maior que numero 2")

if numero1 >= numero2:
    print("O numero 1 é maior ou igual a 2")

if numero1 < numero2:
    print("Numero 1 é menor que numero 2")

if numero1 <= numero2:
    print("Numero 1 é menor ou igual a 2")