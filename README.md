# Dataset analysis
Esse repositório tem como principal finalidade analisar um dataset, recuperando-o do site Kaggle, adicionando-o ao PostgreSQl e trabalhando com seus dados


## Instalação
Para instalar as dependências do projeto, basta executar o comando abaixo:
```bash
python3 -m venv .venv

source .venv/bin/activate #Linux
#or
source .venv/Scripts/activate #Windows

pip install -r requirements.txt

#add kaggle.json inside of scripts folder.

python3 main.py
```