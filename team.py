from database import Database

class Team():
    def __init__(self, id = None, nome = None, ano_fundacao = None, presidente = None, owner_username = None):
        self.database = Database()
        self.id = id
        self.nome = nome
        self.ano_fundacao = ano_fundacao
        self.presidente = presidente
        self.owner_username = owner_username

    def select_all(self):
        result = self.database.execute_query(f'SELECT * FROM time;')

        if(result['error'] != None):
            return {"error": {"Erro" : result['error']['message']}, "status_code": result['error']['status_code']}
        else:
            result = list(result['result'])
            if(len(result) > 0):
                return [{"nome": row[1], "ano_fundacao": row[2], "presidente": row[3]} for row in result]
            else:
                return {}

    def select_by_id(self):
        result = self.database.execute_query(f'SELECT * FROM time WHERE id = {self.id};')

        if(result['error'] != None):
            return {"error": {"Erro" : result['error']['message']}, "status_code": result['error']['status_code']}
        else:
            result = list(result['result'])
            if(len(result) > 0):
                return {"nome": result[0][1], "ano_fundacao": result[0][2], "presidente": result[0][3]}
            else:
                return {}
    
    def select_oldest_team(self):
        result = self.database.execute_query(f'SELECT * FROM time ORDER BY ano_fundacao ASC;')

        if(result['error'] != None):
            return {"error": {"Erro" : result['error']['message']}, "status_code": result['error']['status_code']}
        else:
            result = list(result['result'])
            if(len(result) > 0):
                return {"nome": result[0][1], "ano_fundacao": result[0][2], "presidente": result[0][3]}
            else:
                return {}

    def select_desc_presidente(self):
        result = self.database.execute_query(f'SELECT * FROM time ORDER BY presidente DESC;')

        if(result['error'] != None):
            return {"error": {"Erro" : result['error']['message']}, "status_code": result['error']['status_code']}
        else:
            result = list(result['result'])
            if(len(result) > 0):
                return [{"nome": row[1], "ano_fundacao": row[2], "presidente": row[3]} for row in result]
            else:
                return {}

    def add_time(self):
        result = self.database.execute_query(f'INSERT INTO time (nome, ano_fundacao, presidente, owner_username) VALUES ("{self.nome}", {self.ano_fundacao}, "{self.presidente}", "{self.owner_username}")')

        if(result['error'] != None):
            return {"error": {"Erro" : result['error']['message']}, "status_code": result['error']['status_code']}
        else:
            return {"nome": self.nome, "ano_fundacao": self.ano_fundacao, "presidente": self.presidente}

    def delete_time(self):
        time_para_deletar = self.select_by_id()

        result = self.database.execute_query(f'DELETE FROM time WHERE id={self.id}')

        if(result['error'] != None):
            return {"error": {"Erro" : result['error']['message']}, "status_code": result['error']['status_code']}
        else:
            return time_para_deletar