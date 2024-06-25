"""
Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário
e a porcentagem do aumento. Exiba o valor do aumento e do novo salário.
"""

salario = float(input("Digite o salário: R$"))
porcentagem_aumento = int(input("Digite a porcentagem: "))

valor_aumento = salario * (porcentagem_aumento/100)
novo_salario = salario + valor_aumento

print(f"\nValor do aumento: \tR${valor_aumento:.2f}\nNovo salário: \t\tR${novo_salario:.2f}")
