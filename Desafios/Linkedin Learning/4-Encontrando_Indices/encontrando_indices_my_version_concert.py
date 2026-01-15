"""
Desafio #4
Escreva uma função em Python que determina todos os índices de um determinado numa lista

Entrada: Uma lista para a pesquisa e o valor para ser pesquisado

Saída: Uma lista de índices
"""


def encontrar_indice(lista, valor):
    indice_list = []
    cont = 0
    for item in lista:
        if valor == item:
            indice = lista.index(valor, cont)
            indice_list.append(indice)
            cont = indice + 1

    return indice_list


lista_str = ["Um", "Dois", "Um", "Três", "Um", "Quatro", "Cinco", "Seis", "Um"]
valor_requerido1 = "Um"
print(f"Lista de índices do valor \"{valor_requerido1}\": {encontrar_indice(lista_str, valor_requerido1)}\n")

lista_numero = [20, 30, 20, 40, 80, 110, 20]
valor_requerido2 = 20
print(f"Lista de índices do valor \"{valor_requerido2}\": {encontrar_indice(lista_numero, valor_requerido2)}\n")
