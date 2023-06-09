"""
Nome do Programa: Exercício 013 - Reajuste Salarial
Nome do Autor: Renan Lucas da Silva
Data e Hora: 31.03.23 (18h45)

    EXERCÍCIO 013:
        Receber o salário de um determinado colaborador
        Aplicar um aumento de 15% em seu salário
"""

# entrada
salario = eval(input("Digite o salário do funcionário que receberá um aumento de 15%.\nSalário: "))

# calculo - ESCOLHA UM
aumentado = salario * 1.15
    # decimal
aumentado =salario * 115 / 100
    # regra de três

# saída
print("O colaborador que possuia o salário de R${:.2f} passará a receber um salário de {:.2f}.". format(salario,aumentado))

"""
    SOLUÇÃO:
salario = float(input("Qual é o salário do funcionário? R$"))
novo = salario + (salario * 15 / 100)
print("O funcionário que ganhava R${:.2f}, com 15% de aumento passa a ganhar R${:.2f}.". format(salario,novo))

"""