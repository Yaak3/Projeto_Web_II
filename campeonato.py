import sqlalchemy as db
import json
from database import Database
from sqlalchemy import create_engine

class Campeonato():
    def __init__(self, nome = None, premiacao = None, etapa = None):
        self.database = Database()
        self.nome = nome
        self.premiacao = premiacao
        self.etapa = etapa
    
    def select_by_id(self, id):

        result = self.database.execute_query(f'SELECT * FROM campeonato WHERE campeonato_id = {id};')

        if(len(result) == 0):
            return {}
        elif(len(result) == 1):
            return {"id": result[0][0],"nome": result[0][1], "premiacao": result[0][2], "etapa": result[0][3]}
        else:
            return result

#ver como ajustar esse aqui, vai dar problema
    def select_all(self):

        result = self.database.execute_query(f'SELECT * FROM campeonato;')

        if(len(result) == 1):
            return [{"id": row[0],"nome": row[1], "premiacao": row[2], "etapa": row[3]} for row in result]
        else:
            return result

#ver como ajustar esse aqui, vai dar problema
    def select_by_name(self):

        result = self.database.execute_query(f'SELECT * FROM campeonato WHERE nome LIKE "{self.nome}";')

        if(len(result) == 1):
            return [{"id": row[0],"nome": row[1], "premiacao": row[2], "etapa": row[3]} for row in result]
        else:
            return result

    def select_top_premiacao(self):

        result = self.database.execute_query(f'SELECT * FROM campeonato ORDER BY premiacao desc limit 1;')

        if(len(result) == 0):
            return {}
        elif(len(result) == 1):
            return {"id": result[0][0],"nome": result[0][1], "premiacao": result[0][2], "etapa": result[0][3]}
        else:
            return result


        return result


##Ajustar daqui para baixo
    def add_campeonato(self):
        
        with self.database.connect() as con:

            con.execute(f'INSERT INTO campeonato (nome, premiacao, etapa) VALUES("{self.nome}", "{self.premiacao}", "{self.etapa}")')

        return "Ok"

    def delete_campeoato(self, id):

        with self.database.connect() as con:

            result = con.execute(f'DELETE FROM campeonato WHERE campeonato_id={id}')

        return result

    def update_campeonato(self, id):

        with self.database.connect() as con:

            result = con.execute(f'UPDATE campeonato SET "nome"={self.nome}, "premiacao"={self.premiacao}, "etapa"={self.etapa} WHERE campeonato_id={id}')

        return result