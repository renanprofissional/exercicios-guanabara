"""
Nome do Programa: Exercício 019 - Sorteando um item na lista
Nome do Autor: Renan Lucas da Silva
Data e Hora: 08.06.23 (04h29)

    EXERCÍCIO 19:
        Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
        Faça um programa que ajude ele,
        lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
"""

import random

# entrada de nomes e conversão dos valores em string
nome1 = str(input("Digite o primeiro nome: "))
nome2 = str(input("Digite o segundo nome: "))
nome3 = str(input("Digite o terceiro nome:  "))
nome4 = str(input("Digite o quarto nome: "))

# agrupamento dos nomes em uma lista
alunos = [nome1, nome2, nome3, nome4]

# seleção da um dos itens da lista de maneira randômica
escolhido = random.choice(alunos)

# saída do resultado
print("\n\nO escolhido foi o aluno: {}.\n\nParabens {}!".format(escolhido,escolhido))