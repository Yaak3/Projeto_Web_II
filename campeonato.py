from unicodedata import name
import sqlalchemy as db

class Campeonato:
    def __init__(self, nome, premiacao, etapa=None):
        self.database = db.create_engine(url='127.0.0.1:3306')
        self.database = self.database.connect()
        self.table = db.Table('campeonato')
        self.nome = nome
        self.premiacao = premiacao
        self.etapa = etapa

    def inserir_campeonato(self):
        try:
            insert = db.insert(self.table).values(nome=self.nome, premiacao=self.premiacao, etapa=self.etapa)
            self.database.execute(insert)
        except:
            return False

    def seleciona_um_campeonato(self, id):
        pass