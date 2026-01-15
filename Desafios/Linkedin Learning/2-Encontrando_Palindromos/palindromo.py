"""
Desafio #2
Escreva uma função em Python que determina se um determinado texto é
palíndromo

Entrada: Uma String qualquer

Saída: Um valor booleano (True ou False)
"""

import re


def eh_palindromo(texto: str) -> bool:
    correta = ''.join(re.findall(r'[a-z]+', texto.lower()))
    revertida = correta[::-1]
    return correta == revertida


string = input("Digite uma palavra, frase ou número: ")
msg = eh_palindromo(string)
print(f"A palavra ou frase \"{string}\" é um palíndromo? {msg}")
