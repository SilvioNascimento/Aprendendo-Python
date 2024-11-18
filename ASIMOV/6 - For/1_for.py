# Este código utiliza a estrutura de repetição FOR

lista = [1, 2, 3, 4, 5]
soma = 0

# Para cada valor presente na lista, irá mostrar este valor para o usuário
for valor in lista:
    print(f"Valor: {valor}")

print()

# Para cada valor presente na lista, irá mostrar o seu índice e seu valor para o usuário
for indice, valor in enumerate(lista):
    print(f"Índice {indice}:\tValor: {valor}")
    soma += valor
print(f"Soma total: {soma}")
