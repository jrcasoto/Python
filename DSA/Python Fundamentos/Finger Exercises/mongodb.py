from pymongo import MongoClient
import datetime

# Conectar ao banco de dados
conn = MongoClient('localhost', 27017)
type(conn)

# Criar novo banco de dados (estabelecer conexão)
db = conn.cadastrodb
type(db)

# Criar tabela/collection; os dados só estarão inseridos quando o primeiro documento for inserido
collection = db.cadastrodb
type(collection)

# Criar registro genérico 1
post1 = {"codigo": "ID-123456",
        "prod_name": "Geladeira",
        "marcas": ["Brastemp", "Consul"],
        "data_cadastro": datetime.datetime.utcnow()}

# Inserir registro genérico 1
collection = db.posts
post_id = collection.insert_one(post1)
post_id.inserted_id

# Criar registro genérico 2
post2 = {"codigo": "ID-123457",
        "prod_name": "Televisão",
        "marcas": ["Panasonic", "LG"],
        "data_cadastro": datetime.datetime.utcnow()}

# Inserir registro genérico 2
collection = db.posts
post_id = collection.insert_one(post2)
post_id.inserted_id

# Buscar dados
collection.find_one({"marcas": "LG"})
for post in collection.find():
    print(post)

# Trazer nome do banco e da collection
db.name
db.collection_names()


# ----------------- #

import pymongo

# Quando o localhost não é declarado, os bancos de dados genéricos também são puxados
client_con = pymongo.MongoClient()
client_con.database_names()

db = client_con.cadastrodb
db.collection_names()

# db.create_collection("mycollection")
db.collection_names()

reg = {"Nome": "João Carlos", "Idade": 22}
db.mycollection.insert_one(reg)

db.mycollection.find_one() # Retorna primeiro registro

reg = {"Nome": "Teste", "Idade": 21}
db.mycollection.insert_one(reg)
db.mycollection.find_one()

# Tipos de buscas de dados
col = db["mycollection"]
col.count()
redoc = col.find_one()
redoc