"""
Nome do Programa: Exercício 011 - Pintando Parede
Nome do Autor: Renan Lucas da Silva
Data e Hora: 31.03.23 (17h54)

    EXERCÍCIO 011:
        Receber um valor de 2 dimensões (base e altura)
        Calcular a area do objeto com base nas dimensões
        Calcular quantos litros de tinta serão gastos na área
        Cada 2m^2 carecem de 1L de tinta
"""

# entrada
altura = eval(input("Digite a altura da parede que você quer pintar: "))
base = eval(input("Digite o cumprimento da parede que você quer pintar: "))

# calculos
area = base * altura
tinta = area/2

# saída
print("\nCom base nos dados fornecidos, a parede a ser pintada possui {:.2f}m de altura e {:.2f}m de cumprimento.". format(altura, base))
print("Isso equivale à uma área de {:.2f}m².". format(area))
print("Portanto, serão gastos {:.2f}L de tinta na parede, sabendo que para cada 2m² são gastos 1L de tinta.". format(tinta))
