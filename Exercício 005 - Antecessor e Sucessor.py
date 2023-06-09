"""
Nome do Programa: Exercício 005 - Antecessor e Sucessor
Nome do Autor: Renan Lucas da Silva
Data e Hora: 30.03.23 (16h28)

    EXERCÍCIO 005:
    Faça um programa que leia um número inteiro
    e que mostre na tela o seu antecessor e o seu sucessor.
"""

numero = eval(input("Digite  um número inteiro para verificar seu antecessor e seu sucessor: "))
antec = numero - 1
suces = numero + 1
print("\n\nO número que você digitou foi: {};\nO antecessor deste número é: {};\nO sucessor deste número é: {}.". format(numero, antec, suces))


"""
    SOLUÇÃO:
    
n = int(input("Digite um número: "))
a = n - 1
s = n + 1
print("Analisando o valor {}, seu antecessor é {} e seu sucessor é {}.". format (n, a, s))

    Foi feito com 3 variáveis, uma para cada caso, mas é possível fazer com apenas 1 variável:
    n, n-1 e n+1, todos os casos partindo apenas de "n", não abrindo espaço na memória para "a" ou "s".

"""