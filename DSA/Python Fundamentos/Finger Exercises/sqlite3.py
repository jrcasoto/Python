import os
import sqlite3

os.remove("test.db") if os.path.exists("test.db") else None
# Conectar ao banco de dados (estabelecer conexão e, em seguida, criar um cursor para determinar futuras atividades CRUD)
db = sqlite3.connect("test.db")
cur = db.cursor()


# Criar nova tabela 'teste' no banco de dados
cur.execute("CREATE TABLE teste (id integer primary key, titulo varchar(100), categoria varchar(140))")
cur.execute("CREATE TABLE IF NOT EXISTS produtos(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, date TEXT, prod_name TEXT, valor REAL)")


# Inserir dados a partir de um dicionário de dados
sql_insert = "INSERT INTO teste VALUES (?, ?, ?)"
recset = [(1000, 'a', 'a'), (1001, 'ab', 'ba'), (1002, 'ca', 'ca')]

for rec in recset:
    cur.execute(sql_insert, rec)
cur.execute("INSERT INTO produtos VALUES(10, '2021-05-02 14:32:11', 'Teclado', 90)") # INSERT In-line
db.commit() # Efetivamente grava os registros na tabela


# Visualizar dados inseridos na tabela 'teste'
sql_select = "SELECT * FROM teste"

cur.execute(sql_select)
dados = cur.fetchall()
for row in dados: # Imprime os dados coletados através do método 'fetchall()'
    print(row)


# Fechar cursor e banco de dados (encerrar conexão)
cur.close()
db.close()