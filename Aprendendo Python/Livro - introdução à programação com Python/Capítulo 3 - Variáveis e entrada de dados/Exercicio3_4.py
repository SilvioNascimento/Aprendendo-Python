"""
Escreva uma expressão para determinar se uma pessoa deve ou não pagar imposto. Considere que pagam imposto pessoas cujo salário é maior que R$1200,00
"""

salario_medio = 1200.00
salario_do_usuario = float(input("Digite seu salário: "))

if (salario_do_usuario > salario_medio):
    print("Você irá pagar imposto")
else:
    print("Você não irá pagar imposto")
