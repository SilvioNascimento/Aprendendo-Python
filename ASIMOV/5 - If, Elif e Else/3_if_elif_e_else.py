# Este código é apenas a estrutura de condição IF/ELIF/ELSE

idade = 18
possui_carteira = False

# Se a idade for maior ou igual a 18 e possuir carteira, então execute o bloco de código
if (idade >= 18) and possui_carteira:
    print("Você pode dirigir.")
    a = 10
    print(f"Valor teste: {a}")

# Se apenas possuir a carteira, execute o bloco de código abaixo
elif possui_carteira:
    print("Você apenas possui a carteira. Espere a idade.")

# Se apenas tiver 18 anos ou mais, execute o bloco de código abaixo
elif idade >= 18:
    print("Você já tem 18 anos ou mais de idade. Obtém sua carteira para poder dirigir.")

# Caso as condições acima não forem atendidas, então execute o bloco de código abaixo
else:
    print("Você não pode dirigir.")
