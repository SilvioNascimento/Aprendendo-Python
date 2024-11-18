# Este código será responsável por utilizar valores do tipo lista
# Lista: é um tipo de valor que armazena vários valores como strings, inteiros e booleanos por exemplo

# Criando uma lista com valores
lista = ["Olá", "Silvio", 22, 1.76]

# Mostrando a lista
print(lista)

# Mostrando o tipo de da variável 'lista'
print(type(lista))      # Saída: <class 'list'>

# Acessando um determinado valor de uma lista pelo índice
valor1 = lista[0]       # O índice sempre começa por 0 (zero)
valor2 = lista[1]
print(f"{valor1} {valor2}")

# Informa o tamanho de um valor (seja lista ou uma string)
tamanho_lista = len(lista)
print(f"Tamanho da lista: {tamanho_lista}")
texto = "Um texto qualquer"
tamanho_texto = len(texto)
print(f"Tamanho do texto \'{texto}\': {tamanho_texto}")

# Acessa o último elemento da lista
ultimo_elemento = lista[-1]
print(f"Último elemento: {ultimo_elemento}")

# Slicing de elementos da lista
parte1 = lista[1:3]     # vai pegar os elementos a partir do índice 1 até o índice 2 (3 - 1 = 2)
print(f"1ª parcela: {parte1}")
