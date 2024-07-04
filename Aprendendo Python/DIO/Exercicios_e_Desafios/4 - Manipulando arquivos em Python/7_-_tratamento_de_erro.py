from pathlib import Path
from termcolor import colored

try:
    arquivo = open('outro_arquivo.txt', 'r')

except FileNotFoundError as exc:
    print(colored('Arquivo não encontrado!', 'red'))
    print(exc)

ROOT_PATH = Path(__file__).parent

try:
    arquivo = open(ROOT_PATH / "nova-pasta")
except IsADirectoryError as exc:
    print(colored(f'Não foi possível abrir o arquivo: {exc}', 'red'))
except PermissionError as exc:
    print(colored(f'Você não tem permissão para acessar o arquivo {exc}', 'red'))



