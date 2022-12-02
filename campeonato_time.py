from database import Database


class CampeonatoTime():
    def __init__(self, time_id = None, campeonato_id = None, numero_titulos = None, owner_username = None):
        self.database = Database()
        self.time_id = time_id
        self.campeonato_id = campeonato_id
        self.numero_titulos = numero_titulos
        self.owner_username = owner_username


    def add_campeonato_time(self):
        result = self.database.execute_query(f'INSERT INTO campeonato_time (time_id, campeonato_id, numero_titulos, owner_username) VALUES ("{self.time_id}", {self.campeonato_id}, "{self.numero_titulos}" ,"{self.owner_username}")')

        if(result['error'] != None):
            return {"error": {"Erro" : result['error']['message']}, "status_code": result['error']['status_code']}
        else:
            return {"time_id": self.time_id, "campeonato_id": self.campeonato_id, "numero_titulos": self.numero_titulos}
    