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
        #TESTAR o result[0] pra ver se consegue acessar a tupla
        try:
            result = self.database.execute_query(f'SELECT * FROM campeonato WHERE campeonato_id = {id};')
            result = list(result['result'])

            if(len(result) > 0):
                return {"id": result[0][0],"nome": result[0][1], "premiacao": result[0][2], "etapa": result[0][3]}
            else:
                return {}
        except:
            return {"Erro: " : result['error']['message']}, result['error']['status_code']

    def select_all(self):
        try:
            result = self.database.execute_query(f'SELECT * FROM campeonato;')
            return [{"id": row[0],"nome": row[1], "premiacao": row[2], "etapa": row[3]} for row in result['result']]
        except:
            return {"Erro: " : result['error']['message']}, result['error']['status_code']

    def select_by_name(self):
        try:
            result = self.database.execute_query(f'SELECT * FROM campeonato WHERE nome LIKE "{self.nome}";')
            result = list(result['result'])

            if(len(result) > 0):
                return {"id": result[0][0],"nome": result[0][1], "premiacao": result[0][2], "etapa": result[0][3]}
            else:
                return {}
        except:
            return {"Erro: " : result['error']['message']}, result['error']['status_code']

    def select_top_premiacao(self):
        try:
            result = self.database.execute_query(f'SELECT * FROM campeonato ORDER BY premiacao desc limit 1;')
            result = list(result['result'])

            if(len(result) > 0):
                return {"id": result[0][0],"nome": result[0][1], "premiacao": result[0][2], "etapa": result[0][3]}
            else:
                return {}
        except:
            return {"Erro: " : result['error']['message']}, result['error']['status_code']

    def add_campeonato(self):
        try:
            result = self.database.execute_query(f'INSERT INTO campeonato (nome, premiacao, etapa) VALUES("{self.nome}", "{self.premiacao}", "{self.etapa}")')
            return result['result']
        except:
            return {"Erro: " : result['error']['message']}, result['error']['status_code']


    def delete_campeonato(self, id):
        try:
            selected_to_delete = self.select_by_id(id)

            if(len(selected_to_delete) == 0):
                return {"Message": "O id informado não foi encontrado"}
            
            result = self.database.execute_query(f'DELETE FROM campeonato WHERE campeonato_id={id}')
            return selected_to_delete
        except:
            return {"Erro: " : result['error']['message']}, result['error']['status_code']

    def update_campeonato(self, id):
        try:

            if(self.select_by_id(id) == 0):
                return {"Message": "O id informado não foi encontrado"}
            
            result = self.database.execute_query(f'UPDATE campeonato SET "nome"={self.nome}, "premiacao"={self.premiacao}, "etapa"={self.etapa} WHERE campeonato_id={id}')
            return result

        except:
            return {"Erro: " : result['error']['message']}, result['error']['status_code']