from infra.configs.base import Base
from sqlalchemy import Column, String, Integer, ForeignKey

# Entidades (Tabela no banco de dados que possui atributos)
class Proprietarios(Base):
    __tablename__ = "proprietario"

    id_proprietario = Column(Integer, primary_key=True)
    nome = Column(String, nullable = False)
    cpf = Column(String, nullable = False) 
    idade = Column(String, nullable = False)
    sexo = Column(String, nullable = False)
    id_user = Column(String, ForeignKey("user.id_user"))

    # Método para ser melhor apresentado quando fizer um print()
    def __repr__(self):
        return f"Proprietários [id_user = {self.nome}, id_user = {self.id_user}]"
