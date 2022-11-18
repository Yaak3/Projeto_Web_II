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

            result = {"id": result[0][0],"nome": result[0][1], "premiacao": result[0][2], "etapa": result[0][3]}
        
        return result

    def select_all(self):

        with self.database.connect() as con:

            result = con.execute(f'SELECT * FROM campeonato')

            result = [{"id": row[0],"nome": row[1], "premiacao": row[2], "etapa": row[3]} for row in result]

        return result

    def select_by_name(self):

        with self.database.connect() as con:

            result = con.execute(f'SELECT * FROM campeonato WHERE "nome" LIKE %{self.nome}%')

            result = [{"id": row[0],"nome": row[1], "premiacao": row[2], "etapa": row[3]} for row in result]

        return result

    def select_top_premiacao(self):

        with self.database.connect() as con:

            result = con.execute(f'SELECT * FROM campeonato ORDER BY "premiacao" DESC')

            result = {"id": result[0][0],"nome": result[0][1], "premiacao": result[0][2], "etapa": result[0][3]}

        return result


    def add_campeonato(self):
        
        with self.database.connect() as con:

            result = con.execute(f'INSERT INTO campeonato (nome, premiacao, etapa) VALUES("{self.nome}", "{self.premiacao}", "{self.etapa}")')

        return result

    def delete_campeoato(self, id):

        with self.database.connect() as con:

            result = con.execute(f'DELETE FROM campeonato WHERE campeonato_id={id}')

        return result

    def update_campeonato(self, id):

        with self.database.connect() as con:

            result = con.execute(f'UPDATE campeonato SET "nome"={self.nome}, "premiacao"={self.premiacao}, "etapa"={self.etapa} WHERE campeonato_id={id}')

        return result