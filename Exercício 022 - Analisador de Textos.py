"""
Nome do Programa: Exercício 022 - Analisador de Textos
Nome do Autor: Renan Lucas da Silva
Data e Hora: 08.06.23 (06h22)

    EXERCÍCIO 22:
    Crie um programa que leia o nome completo de uma pessoa e mostre:
    O nome com todas as letras maiúsculas e minúsculas.
    Quantas letras ao todo (sem considerar espaços).
    Quantas letras tem o primeiro nome.
        
"""

# o ".strip()" vai eliminar os espaços que vem antes e depois do nome do usuário
nome = str(input("Digite seu nome inteiro: ")).strip()

# aplicação direto na saída de texto
print("\n\nEste é o seu nome com todas as letras maiúsculas:\n",nome.upper())

# aplicação dentro duma variável, depois printada na saida de texto
nome_min = nome.lower()
print("\n\nEste é o seu nome com todas as letras minúsculas:\n",nome_min)

# o "len" fará a contagem de caracteres e o '- nome.count(" ")' irá tirar o espaço da contagem
nome_letras_quant = len(nome) - nome.count(" ")
print("\n\nQuantas letras tem no seu nome: ", nome_letras_quant)

# o '.find(" ")' vai contar quantas letras existem até o primeiro espaço
print("\n\nSeu primeiro nome tem {} letras.".format(nome.find(" ")))