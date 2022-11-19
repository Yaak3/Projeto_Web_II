import sqlalchemy as db
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError

class Database():
    def __init__(self):
        self.database = create_engine("mysql+pymysql://root:aluno@localhost/webII")

    def execute_query(self, query):
        try:
            with self.database.connect() as con:
                return list(con.execute(query))
        except OperationalError:
            return "Erro ao conectar com o banco de dados", 500