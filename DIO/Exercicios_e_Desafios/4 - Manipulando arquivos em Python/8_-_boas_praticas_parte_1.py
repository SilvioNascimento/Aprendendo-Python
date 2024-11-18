from pathlib import Path


# Pegando o caminho da pasta onde este programa está armazenado
ROOT_PATH = Path(__file__).parent

with open(ROOT_PATH / 'lorem.txt') as arquivo:
    print("Está trabalhando no arquivo")
    print(arquivo.read())
