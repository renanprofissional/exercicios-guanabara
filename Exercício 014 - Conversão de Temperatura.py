"""
Nome do Programa: Exercício 014 - Conversão de Temperatura
Nome do Autor: Renan Lucas da Silva
Data e Hora: 31.03.23 (19h07)

    EXERCÍCIO 014:
        Converter a temperatura de Celsius para Farenheit
"""

# entrada
cel = eval(input("Digite uma temperatura em Graus Celsius: "))

# calculo
far = (cel * 1.8) + 32

# saida
print("O valor digitado era {:.2f} °C e passou a ser {:.2f} °F.". format(cel, far))

print("\n\nENGENHARIA REVERSA: {:.2f}". format((far-32)/1.8))
    # °F pra °C - para verificar se o processo está correto

"""
    SOLUÇÃO:
c = float(input("Informe a temperatura em °C: "))
f = 9 * c / 5 + 32
print("A temperatura de {} °C corresponde a {} °F.". format(c,f))

Devido a ordem de precedencia, não foi necessário nenhum parêntese para organizar o calculo.

"""