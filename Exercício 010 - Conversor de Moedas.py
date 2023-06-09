"""
Nome do Programa: Exercício 010 - Conversor de Moedas
Nome do Autor: Renan Lucas da Silva
Data e Hora: 31.03.23 (14h28)

    EXERCÍCIO 010:
        Faça um programa que leia um valor em reais
        Depois converta esse valor em dólares ( e outras moedas se possível)
"""

real = eval(input("Quanto dinheiro você deseja converter?\nValor em real: "))

dolar = real / 5.07
euro = real/5.51
libra = real/6.26
iene = real/0.038
yuan = real/0.738
    # cotação das moedas em 31.03.23

print("\n\n\nCONVERSÃO DO REAL PARA MOEDAS INTERNACIONAIS\n")
print("O valor em real convertido para dolar é: {:.2f}". format(dolar))
print("O valor em real convertido para euro é: {:.2f}". format(euro))
print("O valor em real convertido para libra é: {:.2f}". format(libra))
print("O valor em real convertido para iene é: {:.2f}". format(iene))
print("O valor em real convertido para yuan é: {:.2f}". format(yuan))

"""
    SOLUÇÃO:
real = float(input("Quanto dinheiro você tem na carteira? "))
dolar = real / 3.27
    # cotação do dólar em 2018
print("Com R$ {:.2f} é possível comprar US$ {:.2f}.". format (real, dolar))

"""