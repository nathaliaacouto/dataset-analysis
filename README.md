# Dataset analysis

Esse repositório tem como principal finalidade analisar um dataset, recuperando-o do site Kaggle, adicionando-o ao PostgreSQl e trabalhando com seus dados

## Instalação

Para instalar as dependências do projeto, basta executar o comando abaixo:

```bash
docker pull postgres

docker run --name postgres_run -e POSTGRES_PASSWORD=password -d -v /tmp:/tmp postgres

docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' postgres_run

#alterar ip do banco baseado no output acima

python3 -m venv .venv

source .venv/bin/activate #Linux
#or
source .venv/Scripts/activate #Windows

pip install -r requirements.txt

#add kaggle.json inside of root folder.

python3 main.py

docker pull metabase/metabase

docker run -d -p 3000:3000 --name metabase metabase/metabase

#configurar no metabase o banco de dados com as mesma credenciais do postgres (main.py)
# localhost:3000 no browser

```
