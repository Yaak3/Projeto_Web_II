import sqlalchemy as db
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
from sqlalchemy.exc import IntegrityError
from sqlalchemy.exc import DataError

class Database():
    def __init__(self):
        self.database = create_engine("mysql+pymysql://projeto_rest@10.10.10.150/projeto_rest")
        self.result = {
            'result': None,
            'error': None
        }

    def execute_query(self, query):
        try:
            with self.database.connect() as con:
                self.result['result'] = con.execute(query)
                return self.result
        except OperationalError as e:
            print(e)
            self.result["error"] = {
                "message": "Erro ao conectar com o banco de dados",
                "status_code": 500
            }

            return self.result 
        except IntegrityError as e:
            self.result["error"] = {
                "message": "Dado não pode ser inserido pois já existe",
                "status_code": 400
            }
            
            return self.result 
        except DataError:
            self.result["error"] = {
                "message": "Tipo do dado incorreto",
                "status_code": 400
            }
            
            return self.result 