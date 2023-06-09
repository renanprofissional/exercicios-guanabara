"""
Nome do Programa: Exercício 009 - Tabuada
Nome do Autor: Renan Lucas da Silva
Data e Hora: 31.03.23 (13h42)

    EXERCÍCIO 009:
        Faça um programa que leia um número qualquer
        e a partir dele faça toda a sua tabuada (de um a dez)
"""

# entrada
num = eval(input("Digite um número para saber sua tabuada: "))

# calculo
um = num*1
dois = num*2
tres = num*3
quatro = num*4
cinco = num*5
seis = num*6
sete = num*7
oito = num*8
nove = num*9
dez = num*10

# saida
print("\n\n\nTABUADA DO NÚMERO {}\n". format(num))
print("1 x {} = {}". format (num,um))
print("2 x {} = {}". format (num,dois))
print("3 x {} = {}". format (num,tres))
print("4 x {} = {}". format (num,quatro))
print("5 x {} = {}". format (num,cinco))
print("6 x {} = {}". format (num,seis))
print("7 x {} = {}". format (num,sete))
print("8 x {} = {}". format (num,oito))
print("9 x {} = {}". format (num,nove))
print("10 x {} = {}". format (num,dez))

"""
    SOLUÇÃO:
num = int(input("Digite um numero para ver sua tabuada: "))
print('{} x {} = {}'. format(num, 1, num*1))
print('{} x {} = {}'. format(num, 2, num*2))
print('{} x {} = {}'. format(num, 3, num*3))
print('{} x {} = {}'. format(num, 4, num*4))
print('{} x {} = {}'. format(num, 5, num*5))
print('{} x {} = {}'. format(num, 6, num*6))
print('{} x {} = {}'. format(num, 7, num*7))
print('{} x {} = {}'. format(num, 8, num*8))
print('{} x {} = {}'. format(num, 9, num*9))
print('{} x {} = {}'. format(num, 10, num*10))

"""