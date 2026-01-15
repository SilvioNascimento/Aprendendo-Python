"""
Desafio #1
Escreva uma função em Python para encontrar os fatores primos que compõe
um número.

Entrada: Número inteiro

Saída: Uma lista com todos os fatores primos
"""


def fatores_primos(number: int) -> list[int]:
    fatores = list()
    divisor = 2
    while divisor <= number:
        if number % divisor == 0:
            fatores.append(divisor)
            number = number // divisor
        else:
            divisor += 1

    return fatores


numero = int(input("Digite um número inteiro: "))
print(f"Os fatores primos do número {numero}: {fatores_primos(numero)}")
