import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / "meu_banco.db")
cursor = conexao.cursor()


def criar_tabela(conexao, cursor):
    cursor.execute('CREATE TABLE IF NOT EXISTS clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), '
                   'email VARCHAR(150))')
    conexao.commit()


def inserir_registro(conexao, cursor, nome, email):
    data = (nome, email)
    cursor.execute('INSERT INTO clientes (nome, email) VALUES (?, ?);', data)
    conexao.commit()


def atualizar_registro(conexao, cursor, nome, email, id):
    data = (nome, email, id)
    cursor.execute('UPDATE clientes SET nome=?, email=? WHERE id=?;', data)
    conexao.commit()


def excluir_registro(conexao, cursor, id):
    data = (id,)
    cursor.execute('DELETE FROM clientes WHERE id=?;', data)
    conexao.commit()


def inserir_registros(conexao, cursor, dados):
    cursor.executemany('INSERT INTO clientes (nome, email) VALUES (?, ?)', dados)
    conexao.commit()


# def recuperar_cliente(cursor, id):
#     data = (id,)
#     cursor.execute('SELECT * FROM clientes WHERE id=?', data)
#     return cursor.fetchone()


def recuperar_cliente(cursor, id):
    cursor.execute('SELECT * FROM clientes WHERE id=?', (id,))
    return cursor.fetchone()


def listar_clientes(cursor):
    cursor.execute('SELECT * FROM clientes')
    return cursor.fetchall()


# Cria a tabela apenas se ela não existir
criar_tabela(conexao, cursor)

# inserir_registro(conexao, cursor, 'Maria Cecilia', 'maria@gmail.com')

# atualizar_registro(conexao, cursor, "Silvio Nascimento Ribeiro", "silvio@gmail.com", 1)

# excluir_registro(conexao, cursor, 2)

# dados = [
#     ('Cicera', 'cicera@gmail.com'),
#     ('Antônia Beatriz', 'beatriz@gmail.com'),
#     ('Jaciel Filho', 'jacielF@gmail.com')
# ]
# inserir_registros(conexao, cursor, dados)

# cliente = recuperar_cliente(cursor, 6)
# print(cliente)

clientes = listar_clientes(cursor)
for row in clientes:
    print(row)
