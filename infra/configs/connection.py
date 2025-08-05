# Conexão com o DB e Sessões
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

# (DBConnectionHandler) Manipulador de Conexão de Banco de Dados
class DBConnectionHandler:
    def __init__(self) -> None:
        self.__connection_string = self.__env_var()
        self.__engine = self.__create_database_engine()
        self.session = None

    # variáveis de ambiente (environment variables)
    def __env_var(self):
        load_dotenv()  # Carrega as variáveis do .env

        user = os.getenv("DB_USER")
        password = os.getenv("DB_PASS")
        host = os.getenv("DB_HOST")
        port = os.getenv("DB_PORT")
        dbname = os.getenv("DB_NAME")
        DATABASE_URL = f"postgresql://{user}:{password}@{host}:{port}/{dbname}"
        return DATABASE_URL


    def __create_database_engine(self):
        engine = create_engine(self.__connection_string)
        return engine
    
    def get_engine(self):
        return self.__engine 

    def __enter__(self):
        print('Iniciando uma Sessão de conexão com o Data Base.')
        session_maker = sessionmaker(bind=self.__engine) # Criando sessões na conexão do DB
        self.session = session_maker() # Abre uma sessão da conexão criada
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Finalizando uma Sessão aberta.')
        self.session.close() # Fecha uma sessão
