import sqlalchemy as db
import json
from sqlalchemy import create_engine

class Campeonato:
    def __init__(self, nome = None, premiacao = None, etapa = None):
        self.database = create_engine("mysql+pymysql://root:aluno@localhost/webII")
        self.nome = nome
        self.premiacao = premiacao
        self.etapa = etapa
    
    def select_by_id(self, id):

        with self.database.connect() as con:

            result = con.execute(f'SELECT * FROM campeonato WHERE campeonato_id = {id}')

            result = [{"nome": row[1], "premiacao": row[2], "etapa": row[3]} for row in result]
        
        return result

    def select_all(self):

        with self.database.connect() as con:

            result = con.execute(f'SELECT * FROM campeonato')

            result = [{"nome": row[1], "premiacao": row[2], "etapa": row[3]} for row in result]

        return result

    def add_campeonato(self):
        
        with self.database.connect() as con:

            result = con.execute(f'INSERT INTO campeonato (nome, premiacao, etapa) VALUES("{self.nome}", "{self.premiacao}", "{self.etapa}")')

            print(result)

        return result