from infra.configs.base import Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

# Entidades (Tabela no banco de dados que possui atributos)
class User(Base):
    __tablename__ = "user"

    id_user = Column(Integer, primary_key=True)
    nome_completo = Column(String, nullable = False)
    email = Column(String, nullable = False) 
    senha = Column(String, nullable = False)
    nome_login = Column(String, nullable = False)
    proprietarios = relationship("Proprietarios", backref="proprietario", lazy="subquery") # Class Proprietarios
    
    def __repr__(self):
        return f"User [id_user = {self.id_user}, email = {self.email}]"
