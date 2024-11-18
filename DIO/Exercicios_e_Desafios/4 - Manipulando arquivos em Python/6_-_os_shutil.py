import os
import shutil
from pathlib import Path


# Pegando o caminho da pasta onde este programa está armazenado
ROOT_PATH = Path(__file__).parent

# os.mkdir(ROOT_PATH / 'nova-pasta')

# arquivo = open(ROOT_PATH / 'novo.txt', 'w')
# arquivo.close()
#
# os.rename(ROOT_PATH / "novo.txt", ROOT_PATH / "alterado.txt")

# os.remove(ROOT_PATH / "alterado.txt")

shutil.move("novo.txt", "nova-pasta")
