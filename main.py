from scripts import manage_db, manage_dataset
import psycopg2

conn = psycopg2.connect(database="postgres", user='postgres',
                        password='password', host='172.17.0.2', port='5432')
# Ativar autocommit para garantir que as alterações sejam aplicadas imediatamente
conn.autocommit = True

# Criar um cursor para executar comandos SQL
cursor = conn.cursor()

# Definir a URL do conjunto de dados
dataset = 'https://www.kaggle.com/datasets/l3llff/banana'

# Definir o caminho do arquivo CSV
csv_file_path = '/tmp/banana_quality.csv'


def main():
    # Job de download do dataset (2)
    print('Job de download do dataset')
    manage_dataset.download_dataset(dataset, csv_file_path)
    print('Job de download do dataset finalizado')

    # Job de criação da tabela
    print('Job de criação da tabela')
    manage_db.create_table(cursor)
    print('Job de criação da tabela finalizado')

    # Job de população da tabela
    print('Job de população da tabela')
    manage_db.populate_table(cursor, csv_file_path)
    print('Job de população da tabela finalizado')

    # Job de seleção de todos os registros
    print('Job de seleção de todos os registros')
    manage_db.select_all(cursor)
    print('Job de seleção de todos os registros finalizado')

    # Fechar o cursor e a conexão com o banco de dados
    cursor.close()
    conn.close()


def reset_workspace():
    # Deletar a tabela "banana" se existir
    manage_db.drop_table(cursor)

    # Deletar o arquivo CSV se existir
    manage_dataset.delete_dataset(csv_file_path)

    cursor.close()
    conn.close()


if __name__ == '__main__':
    reset_workspace = False
    if reset_workspace:
        print('Resetando o ambiente de trabalho...')
        reset_workspace()
        print('Ambiente de trabalho resetado com sucesso!')
    else:
        main()
