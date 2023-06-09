"""
Nome do Programa: Exercício 006 - Dobro, Triplo e Raiz quadrada
Nome do Autor: Renan Lucas da Silva
Data e Hora: 31.03.23 (11h46)

    EXERCÍCIO 006:
        Faça um programa que leia um número inteiro
        e que mostre depois o seu dobro, o seu triplo e a sua raíz quadrada.
"""
import math
numero = eval(input("Digite  um número inteiro para verificar seu dobro, triplo e raiz quadrada: "))
dobro = numero * 2
triplo = numero * 3
raizq = math.sqrt(numero)
print("O número que você digitou é: {};\nO seu dobro é: {};\nO seu triplo é: {};\nA sua raíz quadrada é: {}.". format (numero, dobro, triplo, raizq))

"""
    SOLUÇÃO:

n = int(input("Digite um número: "))
d = n * 2
t = n * 3
r = n ** (1/2)
    # fazer elevado a meio é possível descobrir a raíz quadrada
print("O dobro de {} vale {}.". format (n, d))
print("O triplo de {} vale {}.\nA raíz quadrada vale {:.2f}.". format (n, t, r))

    Foi feito com 3 variáveis, mas é possível derivar todos os outros valores a partir de apenas 1 variável.

"""