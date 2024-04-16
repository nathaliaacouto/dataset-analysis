import os
import opendatasets as od

def download_dataset(dataset_url, dataset_path, csv_file_path):
    if os.path.exists(csv_file_path):
        print(f'O conjunto de dados já foi baixado em {dataset_path}')
        print('Pulando o download...')
    else:
        od.download(dataset_url, dataset_path)
        print(f'O conjunto de dados foi baixado com sucesso em {dataset_path}')

def delete_dataset(csv_file_path):
    if os.path.exists(csv_file_path):
        os.remove(csv_file_path)
        print(f'O conjunto de dados foi removido com sucesso de {csv_file_path}')
    else:
        print(f'O conjunto de dados não existe em {csv_file_path}')