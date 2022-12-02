from database import Database

class Usuario():
    def __init__(self, id=None, username=None, is_editor=None, password=None):
        self.database = Database()
        self.id = id
        self.username = username
        self.is_editor = is_editor
        self.password = password

    def select_usuario_by_login_and_password(self):
        result = self.database.execute_query(f'SELECT * FROM usuario WHERE username LIKE "{self.username}" and password LIKE "{self.password}";')

        if(result['error'] != None):
            return {"error": {"Erro" : result['error']['message']}, "status_code": result['error']['status_code']}
        else:
            result = list(result['result'])
            if(len(result) > 0):
                return {"username": result[0][0], "is_editor": result[0][1]}
            else:
                return {}

    def select_usuario_by_login(self):
        result = self.database.execute_query(f'SELECT * FROM usuario WHERE username LIKE "{self.username}";')

        if(result['error'] != None):
            return {"error": {"Erro" : result['error']['message']}, "status_code": result['error']['status_code']}
        else:
            result = list(result['result'])
            if(len(result) > 0):
                return {"username": result[0][0], "is_editor": result[0][1]}
            else:
                return {}

    def add_usuario(self):
        result = self.database.execute_query(f'INSERT INTO usuario (username, is_editor, password) VALUES ("{self.username}", {self.is_editor}, "{self.password}")')

        if(result['error'] != None):
            return {"error": {"Erro" : result['error']['message']}, "status_code": result['error']['status_code']}
        else:
            return {"username": self.username, "is_editor": self.is_editor}


    def delete_usuario(self):

        usuario_para_deletar = self.select_usuario_by_login()

        result = self.database.execute_query(f'DELETE FROM usuario WHERE username="{self.username}"')

        if(result['error'] != None):
            return {"error": {"Erro" : result['error']['message']}, "status_code": result['error']['status_code']}
        else:
            return usuario_para_deletar
#Ver depois
    def update_usuario(self):

        result = self.database.execute_query(f'UPDATE usuario SET username={self.username}, is_editor={self.is_editor}, password="{self.password}" WHERE username="{self.username}"')

        if(result['error'] != None):
            return {"error": {"Erro" : result['error']['message']}, "status_code": result['error']['status_code']}
        else:
            return {"username": self.username, "is_editor": self.is_editor}