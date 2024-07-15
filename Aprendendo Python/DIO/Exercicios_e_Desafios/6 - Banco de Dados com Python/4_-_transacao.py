import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / "meu_banco.db")
cursor = conexao.cursor()
cursor.row_factory = sqlite3.Row


try:
    cursor.execute('INSERT INTO clientes (nome, email) VALUES (?, ?)', ('Julio', 'julio@gmail.com'))
    cursor.execute('INSERT INTO clientes (nome, email) VALUES (?, ?, ?)', (1, 'Robson', 'Rob@gmail.com'))
    conexao.commit()
except Exception as e:
    print(f'Um erro aconteceu! Error:{e}')
    conexao.rollback()
