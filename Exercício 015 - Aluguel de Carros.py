"""
Nome do Programa: Exercício 015 - Aluguel de Carros
Nome do Autor: Renan Lucas da Silva
Data e Hora: 01.04.23 (21h01)

    EXERCÍCIO 015:
        Escreva um programa que calcule o custo do aluguel de carro
        Peça a quant. de km percorridos
        Peça a quant. de dias alugados
        Precifique em R$ 60 .00 por dia
        Precifique em R$ 0.15 por quilometro percorrido
        Calcule o valor total
"""

# apresentação
print("ALUGUEL DE CARROS\n\n")

# entrada
km = float(input("Quantos quilômetros o cliente percorreu com o carro?\nR: "))
dias = int(input("Quantos dias o cliente fez uso do carro?\nR: "))

# calculos
km_preco = km*0.15
dias_preco = dias*60
total = km_preco + dias_preco

# saida
print("\nO cliente percorreu {:.2f} km durante {} dias com o carro.". format(km,dias))
print("O custo pela distância percorrida é de R$ {:.2f}; o custo pelos dias de uso é de R$ {:.2f}.". format(km_preco,dias_preco))
print("O valor final do aluguel fecha em R$ {:.2f}.". format(total))

"""
    SOLUÇÃO:
dias = int(input("Dias alugados: "))
km = float(input("Km rodados: "))
pago = (dias * 60) + (km * 0.15)
print("O total a pagar é de R$ {:.2f}.". format(pago))

"""