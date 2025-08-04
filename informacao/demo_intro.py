from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os
# Bibliotecas para declarar entidades (declarative base)
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy import Column, String, Integer
# Biblioteca para criação de sessiões 
from sqlalchemy.orm import sessionmaker

#-----------------------------------------
# Configurações
## variável de ambiente
load_dotenv()  # Carrega as variáveis do .env

user = os.getenv("DB_USER")
password = os.getenv("DB_PASS")
host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT")
dbname = os.getenv("DB_NAME")

DATABASE_URL = f"postgresql://{user}:{password}@{host}:{port}/{dbname}"
# Criando engine para conexão com DB
engine = create_engine(DATABASE_URL)
# Declarando a base
Base = declarative_base()

# Criando sessões na conexão do DB
Session = sessionmaker(bind=engine)
# Uma sessão da conexão criada
session = Session()

#-----------------------------------------
# Simples conexão
conn = engine.connect()
# Obtendo informação da tabela com código SQL
response = conn.execute(text("SELECT * FROM public.user;"))
for row in response:
    print(row.email)

# Outra forma de mostrar a mesma informação
print('========================')
with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM public.user;"))
    for row in result:
        print(row)
print('========================')
with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM fazenda;"))
    for row in result:
        print(row)
print('========================')
with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM proprietario;"))
    for row in result:
        print(row)

#----------------------------------------------------------

# Base = declarative_base()

# Entidades
class User(Base):
    __tablename__ = "user"

    id_user = Column(Integer, primary_key=True)
    nome_completo = Column(String, nullable = False)
    email = Column(String, nullable = False) 
    senha = Column(String, nullable = False)
    nome_login = Column(String, nullable = False)
    
    def __repr__(self):
        return f"User [id_user = {self.id_user}, email = {self.email}]"
#----------------------------------------------------------
print('========== QUERY ==============')
# SQL 

## Insert
data_insert = User(nome_completo = "Taluana Tavares", 
                   email = "talu2@gmail.com",
                   senha = '1234',
                   nome_login = "talu")
session.add(data_insert)
session.commit()

## Delete
session.query(User).filter(User.nome_login == "talu").delete()
session.commit()

## Update
session.query(User).filter(User.nome_completo == "Pedro Santos").update({"senha":"12345"})
session.commit()

## Select
data = session.query(User).all()
print(type(data))
print(data)

for row in data:
    print(row)

session.close()
#----------------------------------------------------------

