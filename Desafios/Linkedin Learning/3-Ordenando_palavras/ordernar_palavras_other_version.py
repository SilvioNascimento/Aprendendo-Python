def ordenar_palavras(palavras):
    return ' '.join(sorted(palavras.split(), key=str.casefold))


string = input("Digite palavras: ")
print(ordenar_palavras(string))