import sqlalchemy as db
import json
from sqlalchemy import create_engine

class CampeonatoTime:
    def __init__(self, id_time, id_campeonato):
        self.database = create_engine("mysql+pymysql://root:aluno@localhost/webII")
        self.id_time = id_time
        self.id_campeonato = id_campeonato
    
    