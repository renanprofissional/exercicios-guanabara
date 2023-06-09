"""
Nome do Programa: Exercício 020 - Sorteando uma ordem na lista
Nome do Autor: Renan Lucas da Silva
Data e Hora: 08.06.23 (05h29)

    EXERCÍCIO 20:
        O mesmo professor do desafio 019 quer sortear
        a ordem de apresentação de trabalhos dos alunos.
        Faça um programa que leia o nome dos quatro alunos
        E mostre a ordem sorteada.
"""

import random

print("Olá! A seguir, você digitará quatro nomes para serem ordenados aleatoriamente.\n\n")

nome1 = str(input("Digite o primeio nome: "))
nome2 = str(input("Digite o segundo nome: "))
nome3 = str(input("Digite o terceiro nome: "))
nome4 = str(input("Digite o quarto nome: "))

alunos = [nome1, nome2, nome3, nome4]

random.shuffle(alunos)
print("\n\nA ordem escolhida foi: {}".format(alunos))