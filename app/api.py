from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from scrapping import get_info
from typing import Annotated
from hashlib import sha256
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlmodel import SQLModel, Session, Field, select
import jwt
import os

app = FastAPI()
security = HTTPBearer()

load_dotenv()
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
host = os.getenv("DB_HOST")
database = os.getenv("DB_NAME")

class Usuario(SQLModel, table=True):
    id: int = Field(primary_key=True)    
    nome: str = Field(...)
    email: str = Field(...)
    senha: str = Field(...)

class UserCreate(SQLModel):
    nome: str = Field(...)
    email: str = Field(...)
    senha: str = Field(...)

class Login(SQLModel):
    email: str = Field(...)
    senha: str = Field(...)

engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}/", pool_pre_ping=True)

with engine.connect() as connection:
    connection.execution_options(autocommit=True)
    connection.execute(text(f"CREATE DATABASE IF NOT EXISTS cloud"))

engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}/{database}")

SQLModel.metadata.create_all(engine)  # Recria todas as tabelas

def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]

@app.post("/registrar")
def registro(user: UserCreate, session: SessionDep):
    # Verificar se o usuário já existe
    usuario_existente = session.exec(select(Usuario).where(Usuario.email == user.email)).first()
    if usuario_existente:
        raise HTTPException(status_code=400, detail="Email já registrado")

    # Criar novo usuário
    novo_usuario = Usuario(
        nome=user.nome,
        email=user.email,
        senha=sha256(user.senha.encode()).hexdigest()
    )
    session.add(novo_usuario)
    session.commit()
    session.refresh(novo_usuario)

    # Criar token JWT
    token = jwt.encode(
        payload=novo_usuario.nome,
        key=os.getenv('MINHA_SENHA')
    )
    return {"token": token}

@app.post("/login")
def login(login: Login, session: SessionDep):
    # Buscar o usuário pelo email
    usuario = session.exec(select(Usuario).where(Usuario.email == login.email)).first()

    if not usuario or usuario.senha != sha256(login.senha.encode()).hexdigest():
        raise HTTPException(status_code=401, detail="Credenciais inválidas")

    # Criar token JWT
    token = jwt.encode(
        payload=usuario.nome,
        key=os.getenv('MINHA_SENHA')
    )
    return {"token": token}

def validar_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    try:
        payload = jwt.decode(token, key=os.getenv('MINHA_SENHA'), algorithms=["HS256"])
        return payload
    except:
        raise HTTPException(status_code=403, detail="Token ausente ou inválido")

@app.get("/consultar")
def consulta(user_info: dict = Depends(validar_token)):
    info = get_info()
    return info

    