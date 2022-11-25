from database import Database

class Usuario():
    def __init__(self, id=None, login=None, permicao=None, token_auth=None, password=None):
        self.database = Database()
        self.id = id
        self.login = login
        self.permicao = permicao
        self.is_logado = token_auth
        self.password = password

    def select_usuario_by_id(self):
        try:
            result = self.database.execute_query(f'SELECT * FROM usuario WHERE id = {self.id};')

            result = list(result['result'])

            if(len(result) > 0):
                return {"id": result[0][0], "login": result[0][1], "permicao": result[0][2], "is_logado": result[0][3]}
            else:
                return {}

        except:
            return {"Erro: " : result['error']['message']}, result['error']['status_code']

    def select_usuario_by_login(self):
        try:
            result = self.database.execute_query(f'SELECT * FROM usuario WHERE login = {self.login};')

            result = list(result['result'])

            if(len(result) > 0):
                return {"id": result[0][0], "login": result[0][1], "permicao": result[0][2], "is_logado": result[0][3]}
            else:
                return {}

        except:
            return {"Erro: " : result['error']['message']}, result['error']['status_code']


    def add_usuario(self):
        try:
            result = self.database.execute_query(f'INSERT INTO usuario login, permicao, token_auth, password VALUES({self.login}, {self.permicao}, {self.is_logado}, {self.password}')
            return {"id": self.id, "login": self.login, "permicao": self.permicao}
        except:
            return {"Erro: " : result['error']['message']}, result['error']['status_code']
    
    def delete_usuario(self):
        try:
            result = self.database.execute_query(f'DELETE FROM usuario WHERE id={self.id}')
            return {"id": self.id, "login": self.login, "permicao": self.permicao}
        except:
            return {"Erro: " : result['error']['message']}, result['error']['status_code']

    def update_usuario(self):
        try:
            result = self.database.execute_query(f'UPDATE usuario SET "nome"="{self.login}", "permicao"={self.permicao}, "password"="{self.password}"')
            return {"id": self.id, "login": self.login, "permicao": self.permicao}
        except:
            return {"Erro: " : result['error']['message']}, result['error']['status_code']