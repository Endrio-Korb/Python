import os

from dotenv import load_dotenv

# A função create_engine é utilizada para criar a conexão com o banco de dados
from sqlalchemy import create_engine

# Daqui que vamos utilizar a classe base de onde todas as nossas moelds (classe) herdarão
from sqlalchemy.ext.declarative import declarative_base

# Utilizamos sessionmaker para cirar a sessão de usuário
from sqlalchemy.orm import sessionmaker

# A função load_dotenv carrega as informaãões de um arquivo .env e criar variáveis de ambiente
load_dotenv()

db_user = os.getenv("DB_USER")
db_pass = os.getenv("DB_PASS")
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_name = os.getenv("DB_NAME")

# Utilizamos a connection string na criação da conexão com o banco de dados
# mysql+pymysql -> São a conexão e o driver de conexão
# {db_user}:{db_pass} -> significa o usuáro e a sua senha
# {db_host}:{db_port} -> O endereço onde o banco está rodando e a porta
# {db_name} -> O nome do banco de dados que está sendo feita a conexão
connection_string = f"mysql+pymysql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}"

# Com o código abaixo criar o banco no sqlite3
#connection_string = "sqlite:///db.sqlite3"

# Aqui criamos a conexão com o banco de dados. O primeiro argumento é a connectin string criada
# e o segundo argumento indica que os comandos SQL gerados serão mostrados no terminal
engine = create_engine(connection_string, echo = True)

# Classe base de onde todas as models serão
Base = declarative_base()

# Criamos o objeto de sessão que estará ligado á conexão criada anteriormente
Session = sessionmaker(bind=engine)
session = Session()