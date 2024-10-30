# Sobre o projeto
Esse é o projeto individual da disciplina Computação em nuvem, do 6º semestre de Engenharia de Computação no Insper.
Trata-se de uma estrutura de requisição à API, com autenticação, para obter o **clima diário na cidade de São Paulo**.

Para isso, é realizado web scrapping da [página de clima do G1](https://g1.globo.com/previsao-do-tempo/sp/sao-paulo.ghtml), que se atualiza diariamente. Disso, retira-se as seguintes informações:

1. Data
2. Descrição do clima
3. Temperatura mínima
4. Temperatura máxima

Tais informações são retornadas pela API em um json, conforme demonstrado na aba "Endpoints". O funcionamento básico está exemplificado em um [vídeo no YouTube](https://youtu.be/Yaf96xm-prE?si=9MBDJct9iD-eDBg-)

Realizado pela aluna Ellen Coutinho Lião da Silva.

## Passos para acessar o projeto
1. Clonar e abrir o repositório
2. Executar ```bash docker-compose up -d``` na raiz do projeto

## Estrutura de arquivos

    app/   # Onde os serviços estão alocados
        api.py # Funções e classes que tratam as requisições
        scrapping.py # Função que realiza o WebScrapping
        requirements.txt 
        Dockerfile
    docs/ # Arquivos .md da documentação do projeto
    site/ # Arquivos de renderização da documentação do projeto
    compose.yaml
    mkdocs.yml

## Tecnologias utilizadas
- Docker
- Postgres
- FastAPI
- MKDocs
- Python

## Links relevantes
- [Código fonte](https://github.com/ellencoutinho/api-cloud.git)
- [Vídeo no YouTube](https://youtu.be/Yaf96xm-prE?si=9MBDJct9iD-eDBg-)
- [Imagem no DockerHub](https://hub.docker.com/repository/docker/ellencoutinho/api-clima/general)