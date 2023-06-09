"""
Nome do Programa: Exercício 008 - Conversor de Medidas
Nome do Autor: Renan Lucas da Silva
Data e Hora: 31.03.23 (13h00)

    EXERCÍCIO 008:
        Faça um programa que leia um número em metros de distância
        Converta em quilômetros, hectâmetros, decâmetros, decímetros, centímetros e milímetros.
"""
m = eval(input("Digite uma quantidade de metros para ser convertida: "))

# calculos
km = m/1000
hm = m/100
deca = m/10
m = m
deci = m*10
cm = m*100
mm = m*1000

# saída
print("\n\nO número que você digitou foi: {}.\nO resultado da conversão foi:". format(m))
print("\n{:.3f} quilômetros.\n{:.2f} hectâmetros.\n{:.1f} decâmetros.\n{} metros.\n{} decímetros.\n{} centímetros.\n{} milímetros.". format(km, hm, deca, m, deci, cm, mm))

"""
    SOLUÇÃO:
medida = float(input("Uma distância em metros: "))
cm = medida * 100
mm = medida * 1000
print("A medida de {} em centimetros é {} e em milímetros é {}.". format(medida, cm, mm))

"""