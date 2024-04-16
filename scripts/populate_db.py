import pandas as pd
import psycopg2
from sqlalchemy import create_engine, text
import os
import opendatasets as od

dataset = 'https://www.kaggle.com/datasets/l3llff/banana'

conn = psycopg2.connect(database="postgres", user='postgres', password='password', host='localhost', port='5432')

# Ativar autocommit para garantir que as alterações sejam aplicadas imediatamente
conn.autocommit = True

# Criar um cursor para executar comandos SQL
cursor = conn.cursor()

def create_table(cursor):
    # Definir o comando SQL para criar a tabela "banana" se não existir
    create_table_query = '''CREATE TABLE IF NOT EXISTS banana (
                            size real,
                            weight real, 
                            sweetness real,
                            softness real,
                            harvesttime real,
                            ripeness real,
                            acidity real,
                            quality text
                        );'''

    # Executar o comando para criar a tabela "banana"
    cursor.execute(create_table_query)

# Definir o caminho do arquivo CSV
csv_file_path = '/tmp/banana_quality.csv'

# Definir o comando SQL para carregar os dados do arquivo CSV para a tabela "banana"
copy_query = f'''COPY banana(size, weight, sweetness, softness, harvesttime, ripeness, acidity, quality) 
                FROM '{csv_file_path}' 
                DELIMITER ',' 
                CSV HEADER;'''

# Executar o comando para carregar os dados do arquivo CSV para a tabela "banana"
cursor.execute(copy_query)

# Selecionar todos os registros da tabela "banana" e exibi-los
select_query = '''SELECT * FROM banana;'''
cursor.execute(select_query)
for row in cursor.fetchall():
    print(row)

# Fechar o cursor e a conexão com o banco de dados
cursor.close()
conn.close()