import csv
from pathlib import Path


ROOT_PATH = Path(__file__).parent
COLUNA_ID = 0
COLUNA_NOME = 1

# try:
#     with open(ROOT_PATH / 'usuarios.csv', 'w', encoding='utf-8', newline='') as arquivo:
#         escritor = csv.writer(arquivo)
#         escritor.writerow(['id', 'nome'])
#         escritor.writerow(['1', 'Maria'])
#         escritor.writerow(['2', 'João'])
#
# except IOError as exc:
#     print(f"Erro ao criar o arquivo. {exc}")

try:
    with open(ROOT_PATH / 'usuarios.csv', 'r', encoding='utf-8', newline='') as arquivo:
        leitor = csv.reader(arquivo)
        for row in leitor:
            print(row)
except IOError as exc:
    print(f"Erro ao criar o arquivo. {exc}")


print()

# mostra apenas os valores (tanto do cabeçalho quanto os seus valores), e não uma lista com os mesmos
try:
    with open(ROOT_PATH / 'usuarios.csv', 'r', encoding='utf-8', newline='') as arquivo:
        leitor = csv.reader(arquivo)
        for row in leitor:
            print(row[COLUNA_ID], row[COLUNA_NOME])
except IOError as exc:
    print(f"Erro ao criar o arquivo. {exc}")

print()

# mostra apenas os valores (exceto o do cabeçalho), e não uma lista com os mesmos
try:
    with open(ROOT_PATH / 'usuarios.csv', 'r', encoding='utf-8', newline='') as arquivo:
        leitor = csv.reader(arquivo)
        for idx, row in enumerate(leitor):
            if idx == 0:
                continue
            print(f"ID: {row[COLUNA_ID]}")
            print(f"NOME: {row[COLUNA_NOME]}")
except IOError as exc:
    print(f"Erro ao criar o arquivo. {exc}")

print()

try:
    with open(ROOT_PATH / 'usuarios.csv', 'r', encoding='utf-8', newline='') as arquivo:
        reader = csv.DictReader(arquivo)
        for row in reader:
            print(f"ID: {row['id']}")
            print(f"Nome: {row['nome']}")
except IOError as exc:
    print(f"Erro ao criar o arquivo. {exc}")
