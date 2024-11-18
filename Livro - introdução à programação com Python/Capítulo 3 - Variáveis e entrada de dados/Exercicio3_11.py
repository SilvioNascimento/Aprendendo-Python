"""
Faça um programa que solicite o preço de uma mercadoria e o percentual de desconto. Exiba o
valor do desconto e o preço a pagar
"""

preco = float(input("Digite o preço de uma mercadoria: R$"))
percentual_desconto = int(input("Digite o percentual de desconto: "))

valor_desconto = preco * (percentual_desconto/100)
novo_preco = preco - valor_desconto

print(f"\nValor de desconto: \tR${valor_desconto:.2f}\nNovo preço: \t\tR${novo_preco:.2f}")
