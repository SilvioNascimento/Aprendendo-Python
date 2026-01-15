def encontre_indices(lista, item):
    lista_de_indices = []
    for indice, value in enumerate(lista):
        if value == item:
            lista_de_indices.append([indice])
        elif isinstance(lista[indice], list):
            for i in encontre_indices(lista[indice], item):
                lista_de_indices.append([indice] + i)
    return lista_de_indices

"""
Exemplo 1:
    Entrada: 
        exemplo = [[[1, 2, 3], 2, [1, 3]], [1, 2, 3]]
        valor = 2
        encontre_indices(exemplo, valor)
    
    Saída:
        [[0, 0, 1], [0, 1], [1, 1]]

Exemplo 2:
    Entrada: 
        exemplo = [[[1, 2, 3], 2, [1, 3]], [1, 2, 3]]
        valor = [1, 2, 3]
        encontre_indices(exemplo, valor)
    
    Saída:
        [[0, 0], [1]]
"""
