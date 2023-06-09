"""
Nome do Programa: 021 - Tocando um MP3
Nome do Autor: Renan Lucas da Silva
Data e Hora: 08.06.23 (05h48)

    EXERCÍCIO 21:
        Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
"""

import pygame
pygame.init()
pygame.mixer.music.load("dark-choir-zyzz-hardstyle")




"""
o arquivo de musica precisa estar na mesma pasta que o arquivo de código ".py"
eles precisam ter o mesmo nome, sem acentos, sem caracteres especiais e sem espaços
exemplo: "projeto-abc-123.mp3" & "projeto-abc-123.py" (AMBOS NA MESMA PASTA)

sendo assim, o verdadeiro arquivo deste exercício está nomeado como "dark-choir-zyzz-hardstyle",
    pra não prejudicar a ordenação dos exerc[icios
"""

# ESTTÁ DANDO ERRO NO THONNY, NÃO RECONHECE O MOD PYGAME