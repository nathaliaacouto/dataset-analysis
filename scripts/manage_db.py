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

def populate_table(cursor, csv_file_path):
    # Definir o comando SQL para carregar os dados do arquivo CSV para a tabela "banana"
    copy_query = f'''COPY banana(size, weight, sweetness, softness, harvesttime, ripeness, acidity, quality) 
                    FROM '{csv_file_path}' 
                    DELIMITER ',' 
                    CSV HEADER;'''

    # Executar o comando para carregar os dados do arquivo CSV para a tabela "banana"
    cursor.execute(copy_query)

def drop_table(cursor):
    # Deletar a tabela "banana" se existir
    drop_table_query = '''DROP TABLE IF EXISTS banana;'''
    cursor.execute(drop_table_query)

def select_all(cursor):
    # Selecionar todos os registros da tabela "banana" e exibi-los
    select_query = '''SELECT * FROM banana;'''
    cursor.execute(select_query)
    for row in cursor.fetchall():
        print(row)