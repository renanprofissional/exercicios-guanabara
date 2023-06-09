"""
Nome do Programa: Exercício 007 - Média Aritmética
Nome do Autor: Renan Lucas da Silva
Data e Hora: 30.03.23 (12h23)

    EXERCÍCIO 007:
        Faça um programa que leia dois números inteiros
        Trace uma média a partir dos números obtidos
"""

num_1 = eval(input("Digite o primeiro número: "))
num_2 = eval(input("Digite o segundo número: "))
media = (num_1+num_2)/2
print("Os números digitados foram '{}' & '{}';\nA média aritmética entre esses dois números  é: {}.". format(num_1, num_2, media))

"""
    SOLUÇÃO:
n1 = float(input("Digite o primeiro numero: "))
n2 = float(input("Digite o segundo número: "))
média = (n1 + n2) / 2
print("A média entre {:.1f} e {:.1f} é igual a {:.1f}.". format (n1, n2, média))

"""