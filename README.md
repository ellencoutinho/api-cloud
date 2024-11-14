### API para verificação do clima diário ☀️

Estrutura de requisição a api para obter o clima diário na cidade de São Paulo, com imagem montada e [disponibilizada no docker hub](https://hub.docker.com/repository/docker/ellencoutinho/api-clima/general). O arquivo 
ˋcompose.yamlˋ está na raiz do repositório.

▶️ Funcionamento do docker exemplificado em [vídeo no YouTube](https://youtu.be/Yaf96xm-prE?si=9MBDJct9iD-eDBg-)

▶️ Funcionamento do deploy pela AWS exemplificado em [vídeo no YouTube](https://youtu.be/hM6l0q3O9bU?si=I0sEQQOHafJqHNPe)

#
#### Endpoints da API 👩🏽‍💻

- POST /registrar

    Pode retornar 200 (registro criado com sucesso, com token JWT atribuído no cadastro) ou 409 (quando o email já foi registrado)

- POST /login
    
    Pode retornar 200 (autenticação bem sucedida) ou 401 (o que significa que parte das credenciais estão inválidas)

- GET /consultar

    Pode retornar 200 (autenticação bem sucedida, então retorna as informações do clima) ou 403 (quando o token JWT submetido no header da requisição não é coerente com o token do login)

#

➤ Para mais informações, acesse a [documentação do projeto](https://ellencoutinho.github.io/api-cloud/)

➤ Projeto individual da disciplina Computação em nuvem, do 6º semestre de Engenharia de Computação no Insper. Realizado pela aluna Ellen Coutinho Lião da Silva.