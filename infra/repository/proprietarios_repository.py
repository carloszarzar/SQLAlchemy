from infra.configs.connection import DBConnectionHandler
from infra.entities.proprietario import Proprietarios
from infra.entities.user import User
   
# SQL repository
class ProprietariosRepository:
    # Select
    def select(self):
        with DBConnectionHandler() as db:
            data = db.session\
                .query(Proprietarios)\
                .join(User, Proprietarios.id_user == User.id_user)\
                .with_entities(
                    Proprietarios.nome,
                    Proprietarios.cpf,
                    User.email,
                    User.id_user
                )\
                .all()
            return data
