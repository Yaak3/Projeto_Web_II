from database import Database

class Usuario():
    def __init__(self, id=None, username=None, is_editor=None, password=None):
        self.database = Database()
        self.id = id
        self.username = username
        self.is_editor = is_editor
        self.password = password

    def select_usuario_by_login(self):
        result = self.database.execute_query(f'SELECT * FROM usuario WHERE username LIKE "{self.username}" and password LIKE "{self.password}";')

        if(result['error'] != None):
            return {"error": {"Erro" : result['error']['message']}, "status_code": result['error']['status_code']}
        else:
            result = list(result['result'])
            if(len(result) > 0):
                return {"username": result[0][0], "is_editor": result[0][1]}
            else:
                return {}


'''
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
'''