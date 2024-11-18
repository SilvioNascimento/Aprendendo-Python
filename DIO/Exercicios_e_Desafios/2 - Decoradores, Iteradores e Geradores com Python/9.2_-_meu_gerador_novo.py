def meu_gerador(numeros:list[int]):
    listaNumeros = numeros

    for index in range(len(listaNumeros)):
        listaNumeros[index] *= 2

    yield listaNumeros


for numero in meu_gerador(numeros=[1, 2, 3, 4, 5, 6]):
    print(numero)
