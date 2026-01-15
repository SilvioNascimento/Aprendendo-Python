"""
Exercício #3
Escreva uma função em Python que ordena em ordem alfabética palavras de uma string.

Entrada: Uma string com palavras separadas por um espaço

Saída: Uma string com as palavras em ordem alfabética
"""


def ordenar_palavras(string: str):
    palavras_list = string.split(" ")
    palavras_list = sorted(palavras_list)
    return palavras_list


palavras_str = input("Digite as palavras separadas por espaço: ")
print(ordenar_palavras(palavras_str))
