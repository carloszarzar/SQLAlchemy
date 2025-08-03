from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

load_dotenv()  # Carrega as variáveis do .env

user = os.getenv("DB_USER")
password = os.getenv("DB_PASS")
host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT")
dbname = os.getenv("DB_NAME")

DATABASE_URL = f"postgresql://{user}:{password}@{host}:{port}/{dbname}"

engine = create_engine(DATABASE_URL)
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
