"""
Nome do Programa: Exercício 012 - Calculando Desconto
Nome do Autor: Renan Lucas da Silva
Data e Hora: 31.03.23 (18h18)

    EXERCÍCIO 012:
        Receber o preço de um determinado produto
        Aplicar um desconto de 5% nele
"""

# entrada
preco = eval(input("Digite o preço de um produto que você quer aplicar um desconto de 5%.\nPreço do Produto: "))

# calculo - ESCOLHA UM
descontado = preco*0.95
    # decimal
descontado = preco*95/100
    #regra de três

# saída
print("\n\nCom desconto de 5% OFF, o produto que valia R${:.2f} passa a valer R${:.2f}.". format(preco, descontado))

"""
    SOLUÇÃO:
preco = float(input("Qual é o preço do produto? R$"))
novo = preco - (preco * 5 / 100)
print("O preço que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}.". format(preco,novo))

"""