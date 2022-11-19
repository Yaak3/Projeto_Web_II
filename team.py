import sqlalchemy as db
import json
from sqlalchemy import create_engine

class Team():
    def __init__(self, nome = None, ano = None):
        self.database = create_engine("mysql+pymysql://root:aluno@localhost/webII")
        self.nome = nome
        self.ano = ano
    
    def select_by_id(self, id):

        with self.database.connect() as con:

            result = con.execute(f'SELECT * FROM time WHERE campeonato_id = {id}')

            result = {"id": result[0][0],"nome": result[0][1], "ano": result[0][2]}
        
        return result

    def select_all(self):

        with self.database.connect() as con:

            result = con.execute(f'SELECT * FROM time')

            result = [{"nome": row[1], "ano": row[2]} for row in result]

        return result

    def select_by_name(self):

        with self.database.connect() as con:

            result = con.execute(f'SELECT * FROM time WHERE "nome" LIKE %{self.nome}%')

            result = [{"id": row[0],"nome": row[1], "ano": row[2]} for row in result]

        return result

    def select_oldest_team(self):

        with self.database.connect() as con:

            result = con.execute(f'SELECT * FROM campeonato ORDER BY "ano" ASC')

            result = {"id": result[0][0],"nome": result[0][1], "ano": result[0][2]}

        return result


    def add_team(self):
        
        with self.database.connect() as con:

            result = con.execute(f'INSERT INTO campeonato (nome, ano) VALUES("{self.nome}", "{self.ano}")')

        return result

    def delete_campeoato(self, id):

        with self.database.connect() as con:

            result = con.execute(f'DELETE FROM campeonato WHERE time_id={id}')

        return result

    def update_campeonato(self, id):

        with self.database.connect() as con:

            result = con.execute(f'UPDATE campeonato SET "nome"={self.nome}, "ano"={self.ano} WHERE time_id={id}')

        return result