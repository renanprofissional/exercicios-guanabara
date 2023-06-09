"""
Nome do Programa: Exercício 017 - Calculando hipotenusa
Nome do Autor: Renan Lucas da Silva
Data e Hora: 08.06.23 (03h51)

    EXERCÍCIO 017:
        Faça um programa que leia o comprimento do cateto oposto
        Leia o cateto adjacente de um triângulo retângulo.
        Calcule e mostre o comprimento da hipotenusa.
"""

import math

print("SEJA BEM VINDO A CALCULADORA DE HIPOTENUSA!")
print("\n\n\nUma hipotenusa é o cumprimento oposto ao angulo reto de um trangulo retangulo, ao lado de dois outros cumprimentos chamados de catetos: cateto oposto e cateto adjacente.")
cat_oposto = eval(input("\nDigite um valor para o cumprimento do cateto oposto: "))
cat_adjacente = eval(input("Digite o valor para o cumprimento do cateto adjacente: "))

hipotenusa = math.sqrt (cat_oposto**2+cat_adjacente**2)
hipotenusa2 = (cat_oposto**2+cat_adjacente**2)**0.5


print("Parabéns! O resultado da sua hipotenusa em 'math' é: ", hipotenusa)
print("O resultado da hipotenusa em elevação a o.5 é: ", hipotenusa2)