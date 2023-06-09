"""
Nome do Programa: Exercício 018 - Seno, Cosseno e Tangente
Nome do Autor: Renan Lucas da Silva
Data e Hora: 08.06.23 (04h29)

    EXERCÍCIO 18:
        Faça um programa que leia um ângulo qualquer
        Mostre na tela o valor do seno, cosseno e tangente desse ângulo
"""

import math

# aqui é pegado  o valor em graus
angulo = float(input("Digite o angulo que voce deseja: "))

# aqui é convertido o valor de graus para radiano e calculado o seno em cima do radiano
seno = math.sin(math.radians(angulo))

# aqui é a saida dos valores formatada por 'format'
print("O angulo de {} tem o SENO de {:.2f}.".format(angulo,seno))

# do angulo se converte a radiano e deste, calculado o cosseno; depois é printado os valores com 'format'
cosseno = math.cos(math.radians(angulo))
print("O angulo de {} possui o COSSENO de {:.2f}.".format(angulo,cosseno))


# do angulo se converte em radiano, do radiano se calcula a tangente, da tangente se printa com 'format'
tangente = math.tan(math.radians(angulo))
print("O angulo de {} possui a TANGENTE de {:.2f}.".format(angulo,tangente))
