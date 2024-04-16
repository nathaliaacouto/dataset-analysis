from scripts import populate_db
import psycopg2

def main():
    conn = psycopg2.connect(database="postgres", user='postgres', password='password', host='localhost', port='5432')

    # Ativar autocommit para garantir que as alterações sejam aplicadas imediatamente
    conn.autocommit = True

    # Criar um cursor para executar comandos SQL
    cursor = conn.cursor()
    pass
















if __name__ == '__main__':
    main()