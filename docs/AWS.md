# Deploy dos serviços no EKS da AWS

Foi realizado o deploy dos dois serviços para o funcionamento da aplicação:

1. **Banco de Dados (PostgreSQL)**
2. **API de Clima** — A API fornece informações sobre o clima atual, detalhada na seção Endpoints desse site. Ela pode ser acessada através da URL:
```
http://a9ec7415777414057a984d4103f0432e-374415893.us-east-1.elb.amazonaws.com:8000/docs
```

[Clique aqui para acessar a API](http://a9ec7415777414057a984d4103f0432e-374415893.us-east-1.elb.amazonaws.com:8000/docs)

[Clique aqui para visualizar o vídeo de demonstração](https://youtu.be/hM6l0q3O9bU?si=I0sEQQOHafJqHNPe)

---

## Tecnologia Utilizada

Para realizar o deploy, foi utilizado o **Elastic Kubernetes Service (EKS)** e **Kubernetes** da AWS, onde cada serviço foi implantado em um **POD**. A estrutura de rede também foi provida pela AWS, no serviço de infraestrutura como código, [endereçada no link](https://www.youtube.com/redirect?event=comments&redir_token=QUFFLUhqbGZZRDRlbjlKVWp1NlpSUTJpelg1QVJvWGlWZ3xBQ3Jtc0ttODhqdUIxcjVuc0lNLXFTQ1owWDVfQ1d4clI5d05EY0dVbW9mSXhxX1ZvUTY5LVJtWm1oUTFmOENNWURsa0ZGa0FhS2NTMW9WUzN0eFBUa19aMF91Y2dmSVdEc0U0MFdVTDQwWk5XeFZ5ZlU0VTZFaw&q=https%3A%2F%2Fs3.us-west-2.amazonaws.com%2Famazon-eks%2Fcloudformation%2F2020-10-29%2Famazon-eks-vpc-private-subnets.yaml).


Abaixo estão os arquivos de configuração que foram utilizados, os quais estão também disponíveis no [repositório do projeto](https://github.com/ellencoutinho/api-cloud.git).

---

## Arquivos de Configuração

#### 1. **api-deployment.yaml**
Este arquivo configura o deploy da API que serve os dados sobre o clima.

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: api-deployment
spec:
  replicas: 1
  selector:
    matchLabels:
      app: api
  template:
    metadata:
      labels:
        app: api
    spec:
      containers:
      - name: api-container
        image: ellencoutinho/api-clima:v5
        env:
        - name: DB_USER
          value: "projeto"
        - name: DB_PASSWORD
          value: "projeto"
        - name: DB_HOST
          value: "db-service"
        - name: DB_NAME
          value: "projeto"
        - name: MINHA_SENHA
          value: "projeto"
        ports:
        - containerPort: 8000
---
apiVersion: v1
kind: Service
metadata:
  name: api-service
spec:
  selector:
    app: api
  ports:
    - port: 8000
      targetPort: 8000
  type: LoadBalancer
```

#### 2. **db-deployment.yaml**
Este arquivo configura o deploy do banco de dados PostgreSQL, que armazena as informações necessárias para a API.
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: db-deployment
spec:
  replicas: 1
  selector:
    matchLabels:
      app: db
  template:
    metadata:
      labels:
        app: db
    spec:
      containers:
      - name: db-container
        image: postgres:16
        env:
        - name: POSTGRES_DB
          value: "projeto"
        - name: POSTGRES_USER
          value: "projeto"
        - name: POSTGRES_PASSWORD
          value: "projeto"
        ports:
        - containerPort: 5432
---
apiVersion: v1
kind: Service
metadata:
  name: db-service
spec:
  selector:
    app: db
  ports:
    - port: 5432
      targetPort: 5432
```