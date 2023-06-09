"""
Nome do Programa: Exercício 016 - Quebrando um número
Nome do Autor: Renan Lucas da Silva
Data e Hora: 01.04.23 (21h33)

    EXERCÍCIO 016:
        Crie um programa que leie um numero real qualquer
        Converta o real para inteiro na saída
"""

real01 = (eval(input("Digite um número decimal para muda-lo na ENTRADA com EQUAÇÃO.\nR: ")))//1
print("O número passou a ser: ", (real01))
    # aqui ele fica inteiro, mas na saída ainda sobra uma casa decimal, ainda que zerada.

real00 = eval(input("\nDigite um número decimal para muda-lo no MEIO por EQUAÇÃO.\nR: "))
real00 = real00//1
print("O número passou a ser: ", (real00))
    # aqui ele fica inteiro, mas na saída ainda sobra uma casa decimal, ainda que zerada.

real04 = float(input("\nDigite um número decimal para muda-lo no MEIO com NOVA VARIÁVEL.\nR: "))
real04_int = int(real04)
print("O número passou a ser: ", (real04_int))

real02 = float(input("\nDigite um número decimal para muda-lo na SAÍDA com FORMAT.\nR: "))
print("O número passou a ser: {:.0f}.". format(real02))

real03 = eval(input("\nDigite um número decimal para muda-lo na SAÍDA com INT.\nR: "))
print("O número passou a ser: ", (int(real03)))

"""
    SOLUÇÃO:
import math
num = float(input("Digite um valor: "))
print("O valor digitado foi {} e a sua porção inteira é {}.". format (num, math.trunc(num)))

"""