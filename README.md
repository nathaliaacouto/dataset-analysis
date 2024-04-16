# Dataset analysis

Esse repositório tem como principal finalidade analisar um dataset, recuperando-o do site Kaggle, adicionando-o ao PostgreSQl e trabalhando com seus dados

## Instalação

Para instalar as dependências do projeto, basta seguir o passo a passo abaixo:

1. Caso não tenha o postgreSQL instalado, use a versão do Docker, com os comandos
```bash
$ docker pull postgres

$ docker run --name postgres_run -e POSTGRES_PASSWORD=password -d -v /tmp:/tmp postgres

$ docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' postgres_run

#alterar ip do banco baseado no output acima
```
2. Clone o projeto na sua máquina:
```
$ git clone https://github.com/nathaliaacouto/dataset-analysis.git
```
3. Abra um ambiente virtual com python:
```
$ python3 -m venv .venv

$ source .venv/bin/activate #Linux
#or
$ source .venv/Scripts/activate #Windows
```
4. Instale o que é necessário para rodar o programa:
```
$ pip install -r requirements.txt
```
5. Para utilizar a API do Kaggle, vc precisa de um arquivo kaggle.json, que é possível de conseguir pela área de perfil no próprio site, adicione-o ao projeto.
6. Faça as configurações finais, rodando também o metabase (se não o tiver, utilize o docker):
```
$ python3 main.py

$ docker pull metabase/metabase

$ docker run -d -p 3000:3000 --name metabase metabase/metabase
```
7. Configure no metabase o banco de dados com as mesma credenciais do postgres (main.py)
8. Finalmente, acesse localhost:3000 no browser de sua preferência

Observação: Esse passo a passo foi feito em um sistema Linux, com contâiners Docker (estando esse já instalado), recomendamos a utilização dessas tecnologias para melhor funcionamento do projeto.
