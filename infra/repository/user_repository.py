from infra.configs.connection import DBConnectionHandler
from infra.entities.user import User

# SQL repository
class UserRepository:
    # Select
    def select(self):
        with DBConnectionHandler() as db:
            data = db.session.query(User).all()
            return data
    # Insert
    def insert(self, nome_completo, email, senha, nome_login):
        with DBConnectionHandler() as db:
            data_insert = User(nome_completo = nome_completo, 
                   email = email,
                   senha = senha,
                   nome_login = nome_login)
            db.session.add(data_insert)
            db.session.commit()

    # Delete
    def delete(self, nome_login):
        with DBConnectionHandler() as db:
            db.session.query(User).filter(User.nome_login == nome_login).delete()
            db.session.commit()
        
    # Update
    def update(self, nome_completo, senha):
        with DBConnectionHandler() as db:
            db.session.query(User).filter(User.nome_completo == nome_completo).update({"senha":senha})
            db.session.commit()
