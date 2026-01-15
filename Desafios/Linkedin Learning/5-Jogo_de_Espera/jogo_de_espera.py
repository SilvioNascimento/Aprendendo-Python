"""
Desafio #5
Jogo de Espera
"""

from time import perf_counter
from random import randint


def jogo_de_espera():
    tempo_aleatorio = randint(2, 4)
    print(f"Seu objetivo é de {tempo_aleatorio} segundo(s)")
    opcao = input("---Pressione Enter para começar---\n")

    while opcao != '':
        opcao = input("Opção inválida! Por favor, pressione Enter para começar\n")

    inicio = perf_counter()

    opcao_finalizar = input(f"...Pressione Enter de novo depois de {tempo_aleatorio} segundo(s)...")

    while opcao_finalizar != '':
        opcao_finalizar = input("Opção inválida! Por favor, pressione Enter\n")

    fim = perf_counter()
    tempo_decorrido = fim - inicio
    print(f"Tempo decorrido: {tempo_decorrido:.3f}")

    if tempo_decorrido < tempo_aleatorio:
        tempo_sobrando = tempo_aleatorio - tempo_decorrido
        print(f"Iiii... Rápido demais... Sobrou ({tempo_sobrando:.3f})")

    elif tempo_decorrido > tempo_aleatorio:
        tempo_ultrapassado = tempo_decorrido - tempo_aleatorio
        print(f"Iiii... Devagar demais... Sobrou ({tempo_ultrapassado:.3f})")

    else:
        print("Conseguiu!!! Meus parabéns!")


jogo_de_espera()

