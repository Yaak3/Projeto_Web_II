from database import Database

class Campeonato():
    def __init__(self, id=None, nome = None, premiacao = None, etapa = None, owner_username = None):
        self.database = Database()
        self.id = id
        self.nome = nome
        self.premiacao = premiacao
        self.etapa = etapa
        self.owner_username = owner_username
    
    def select_all(self):
        result = self.database.execute_query(f'SELECT * FROM campeonato;')

        if(result['error'] != None):
            return {"error": {"Erro" : result['error']['message']}, "status_code": result['error']['status_code']}
        else:
            result = list(result['result'])
            if(len(result) > 0):
                return [{"nome": row[1], "premiacao": row[2], "etapa": row[3]} for row in result]
            else:
                return {}

    def select_by_id(self):
        result = self.database.execute_query(f'SELECT * FROM campeonato WHERE id = {self.id};')

        if(result['error'] != None):
            return {"error": {"Erro" : result['error']['message']}, "status_code": result['error']['status_code']}
        else:
            result = list(result['result'])
            if(len(result) > 0):
                return {"nome": result[0][1], "premiacao": result[0][2], "epata": result[0][3]}
            else:
                return {}

    def select_order_by_name(self):
        result = self.database.execute_query(f'SELECT * FROM campeonato ORDER BY nome ASC;')

        if(result['error'] != None):
            return {"error": {"Erro" : result['error']['message']}, "status_code": result['error']['status_code']}
        else:
            result = list(result['result'])
            print(result)
            if(len(result) > 0):
                return [{"nome": row[1], "premiacao": row[2], "etapa": row[3]} for row in result]
            else:
                return {}

    def select_top_premiacao(self):
        result = self.database.execute_query(f'SELECT * FROM campeonato ORDER BY premiacao DESC;')

        if(result['error'] != None):
            return {"error": {"Erro" : result['error']['message']}, "status_code": result['error']['status_code']}
        else:
            result = list(result['result'])
            if(len(result) > 0):
                return {"nome": result[0][1], "premiacao": result[0][2], "epata": result[0][3]}
            else:
                return {}

    def add_campeonato(self):
        result = self.database.execute_query(f'INSERT INTO campeonato (nome, premiacao, etapa, owner_username) VALUES ("{self.nome}", {self.premiacao}, "{self.etapa}", "{self.owner_username}")')

        if(result['error'] != None):
            return {"error": {"Erro" : result['error']['message']}, "status_code": result['error']['status_code']}
        else:
            return {"nome": self.nome, "premiacao": self.premiacao, "etapa": self.etapa}

    def delete_campeonato(self):
        campeonato_para_deletar = self.select_by_id()

        result = self.database.execute_query(f'DELETE FROM campeonato WHERE id="{self.id}"')

        if(result['error'] != None):
            return {"error": {"Erro" : result['error']['message']}, "status_code": result['error']['status_code']}
        else:
            return campeonato_para_deletar