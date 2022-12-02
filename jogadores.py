from database import Database

class Jogadores():
    def __init__(self, id = None, nome = None, salario = None, valor_mercado = None, time_id = None, owner_username = None):
        self.database = Database()
        self.id = id
        self.nome = nome
        self.salario = salario
        self.valor_mercado = valor_mercado
        self.time_id = time_id
        self.owner_username = owner_username

    def select_all(self):
        result = self.database.execute_query(f'SELECT * FROM jogadores;')

        if(result['error'] != None):
            return {"error": {"Erro" : result['error']['message']}, "status_code": result['error']['status_code']}
        else:
            result = list(result['result'])
            if(len(result) > 0):
                return [{"nome": row[1], "salario": row[2], "valor_mercado": row[3], "time_id": row[4]} for row in result]
            else:
                return {}

    def select_by_id(self):
        result = self.database.execute_query(f'SELECT * FROM jogadores WHERE id = {self.id};')

        if(result['error'] != None):
            return {"error": {"Erro" : result['error']['message']}, "status_code": result['error']['status_code']}
        else:
            result = list(result['result'])
            if(len(result) > 0):
                return {"nome": result[0][1], "salario": result[0][2], "valor_mercado": result[0][3], "time_id": result[0][4]}
            else:
                return {}

    def select_maior_salario(self):
        result = self.database.execute_query(f'SELECT * FROM jogadores ORDER BY salario DESC;')

        if(result['error'] != None):
            return {"error": {"Erro" : result['error']['message']}, "status_code": result['error']['status_code']}
        else:
            result = list(result['result'])
            if(len(result) > 0):
                return {"nome": result[0][1], "salario": result[0][2], "valor_mercado": result[0][3], "time_id": result[0][4]}
            else:
                return {}

    def select_menor_valor_mercado(self):
        result = self.database.execute_query(f'SELECT * FROM jogadores ORDER BY valor_mercado ASC;')

        if(result['error'] != None):
            return {"error": {"Erro" : result['error']['message']}, "status_code": result['error']['status_code']}
        else:
            result = list(result['result'])
            if(len(result) > 0):
                return {"nome": result[0][1], "salario": result[0][2], "valor_mercado": result[0][3], "time_id": result[0][4]}
            else:
                return {}

    def add_jogador(self):
        result = self.database.execute_query(f'INSERT INTO jogadores (nome, salario, valor_mercado, time_id, owner_username) VALUES ("{self.nome}", {self.salario}, "{self.valor_mercado}", {self.time_id} ,"{self.owner_username}")')

        if(result['error'] != None):
            return {"error": {"Erro" : result['error']['message']}, "status_code": result['error']['status_code']}
        else:
            return {"nome": self.nome, "salario": self.salario, "valor_mercado": self.valor_mercado}

    def delete_jogador(self):
        jogador_para_deletar = self.select_by_id()

        result = self.database.execute_query(f'DELETE FROM jogadores WHERE id={self.id}')

        if(result['error'] != None):
            return {"error": {"Erro" : result['error']['message']}, "status_code": result['error']['status_code']}
        else:
            return jogador_para_deletar