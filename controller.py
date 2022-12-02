from flask import Flask
from flask import request
from team import Team
from campeonato import Campeonato
from usuario import Usuario
import pendulum
from datetime import datetime
import jwt
from jwt import DecodeError
import json
from json import JSONDecodeError


app = Flask(__name__)


@app.route("/login", methods=["GET"])
def login_user():
    auth = dict(request.headers)

    if('Authorization' not in auth.keys()):
        return {"Erro": "Usuário ou senha não informados"} , 400
    elif('Basic' not in auth['Authorization']):
        return {"Erro": "Usuário ou senha não informados"} , 400
    else:
        auth = request.authorization

    usuario = Usuario(username=auth['username'], password=auth['password'])

    usuario = usuario.select_usuario_by_login_and_password()

    if("error" in usuario.keys()):
        return usuario["error"], usuario["status_code"]
    else:
        if(len(usuario) > 1):
                
            expire_date = pendulum.now()
            
            expire_date = expire_date.add(minutes=5)

            usuario["expire_date"] = datetime.timestamp(expire_date)

            return {'token': jwt.encode(payload=usuario, key="projeto_rest"), 'expira_em': usuario["expire_date"]}
            
    return {"Erro": "Usuário ou senha não encontrados"}, 401

def verifica_identidade(headers):
    auth = dict(headers)

    if('Authorization' not in auth.keys()):
        return {"error": {"Erro": "Token não informado"}, "status_code": 400}
    elif('Bearer' not in auth['Authorization']):
        return {"error": {"Erro": "Token não informado"}, "status_code": 400}
    else:
        auth = headers["Authorization"]

    auth = auth.split()

    try:
        auth = jwt.decode(auth[1], algorithms=['HS256'], key="projeto_rest")
    except DecodeError:
        return {"error": {"Erro": "Token informado não é valido"}, "status_code": 401}
    except:
        return {"error": {"Erro": "Token informado não é valido"}, "status_code": 401}

    usuario = Usuario(username=auth["username"])
    usuario = usuario.select_usuario_by_login()

    if(len(usuario) > 1):
        return {"result": {"is_editor": auth['is_editor'], "username": auth["username"]}}
    else:
        return {"error": {"Erro": "Usuário não existe"}, "status_code": 401}
        
@app.route("/usuario", methods=["POST"])
def add_user():
    identidade = verifica_identidade(request.headers)

    if("error" in identidade.keys()):
        return identidade["error"], identidade['status_code']

    if(identidade["result"]["is_editor"] != 1):
        return {"Erro": "Seu usuário não tem permissão para adicionar outros usuários"}, 401
    
    try:
        data = json.loads(request.data)
    except:
        return {"Erro": "Request inválida"}, 400

    if('username' not in data.keys() or 'is_editor' not in data.keys() or 'password' not in data.keys()):
        return {"Erro": "Dados faltando na request!"}, 400

    if(data['username'] != "" and  data['username'] != None and data['is_editor'] != "" and data['is_editor'] != None and data['password'] != "" and data["password"] != None):
        usuario = Usuario(username=data['username'], is_editor=data['is_editor'], password=data['password'])
        usuario = usuario.add_usuario()

        if("error" in usuario):
            return usuario["error"], usuario["status_code"]
        else:
            return usuario

    else:
        return {"Erro": "Dados inválidos na request"}, 400

@app.route("/usuario/<string:user>", methods=["DELETE"])
def delete_usuario(user):

    usuario = Usuario(username=user)
    usuario = usuario.select_usuario_by_login()

    if(len(usuario) > 1):
        usuario = Usuario(username=user)
        usuario = usuario.delete_usuario()

        if("error" in usuario):
            return usuario["error"], usuario["status_code"]
        else:
            return usuario
    else:
        return {"Erro" : "Usuário não encontrado"}, 404

#Ver depois
@app.route("/usuario/<string:user>", methods=["PATCH"])
def update_usuario(user):
    identidade = verifica_identidade(request.headers)

    if("error" in identidade.keys()):
        return identidade["error"], identidade['status_code']

    if(identidade["result"]["is_editor"] != 1):
        return {"Erro": "Seu usuário não tem permissão para adicionar outros usuários"}, 401
    
    try:
        data = json.loads(request.data)
    except:
        return {"Erro": "Request inválida"}, 400

    if('username' not in data.keys() or 'is_editor' not in data.keys() or 'password' not in data.keys()):
        return {"Erro": "Dados faltando na request!"}, 400

    if(data['username'] != "" and  data['username'] != None and data['is_editor'] != "" and data['is_editor'] != None and data['password'] != "" and data["password"] != None):

        usuario = Usuario(username=user)
        usuario = usuario.select_usuario_by_login()

        if(len(usuario) > 1):

            usuario = Usuario(username=data['username'], is_editor=data['is_editor'], password=data['password'])
            usuario = usuario.update_usuario()
        
        else:
            return {"Erro" : "Usuário não encontrado"}, 404

        if("error" in usuario):
            return usuario["error"], usuario["status_code"]
        else:
            return usuario

    else:
        return {"Erro": "Dados inválidos na request"}, 400


#Campeonato
@app.route("/campeonato", methods=["GET"])
def select_all_campeonatos():
    campeonato = Campeonato()
    campeonato = campeonato.select_all()

    if("error" in campeonato):
        return campeonato["error"], campeonato["status_code"]
    else:
        return campeonato

@app.route("/campeonato/<int:id>", methods=["GET"])
def select_campeonato(id):
    campeonato = Campeonato(id = id)
    campeonato =  campeonato.select_by_id()

    if("error" in campeonato):
        return campeonato["error"], campeonato["status_code"]
    else:
        return campeonato

@app.route("/campeonato/order_by_nome")
def select_order_by_nome():
    campeonato = Campeonato()
    campeonato = campeonato.select_order_by_name()

    if("error" in campeonato):
        return campeonato["error"], campeonato["status_code"]
    else:
        return campeonato

@app.route("/campeonato/select_top_premiacao")
def select_top_premiacao():
    campeonato = Campeonato()
    campeonato = campeonato.select_top_premiacao()

    if("error" in campeonato):
        return campeonato["error"], campeonato["status_code"]
    else:
        return campeonato

@app.route("/campeonato", methods=["POST"])
def add_campeonato():
    identidade = verifica_identidade(request.headers)

    if("error" in identidade.keys()):
        return identidade["error"], identidade['status_code']

    if(identidade["result"]["is_editor"] != 1):
        return {"Erro": "Seu usuário não tem permissão para adicionar campeonatos"}, 401
    
    try:
        data = json.loads(request.data)
    except:
        return {"Erro": "Request inválida"}, 400

    if('nome' not in data.keys() or 'premiacao' not in data.keys() or 'etapa' not in data.keys()):
        return {"Erro": "Dados faltando na request!"}, 400

    if(data['nome'] != "" and  data['nome'] != None and data['premiacao'] != "" and data['premiacao'] != None and data['etapa'] != "" and data["etapa"] != None):
        
        campeonato = Campeonato(nome=data['nome'], premiacao=data['premiacao'], etapa=data['etapa'], owner_username=identidade['result']["username"])
        campeonato = campeonato.add_campeonato()

        if("error" in campeonato):
            return campeonato["error"], campeonato["status_code"]
        else:
            return campeonato

    else:
        return {"Erro": "Dados inválidos na request"}, 400

@app.route("/campeonato/<int:id>", methods=["DELETE"])
def delete_campeonato(id):
    campeonato = Campeonato(id=id)
    campeonato = campeonato.select_by_id()

    if(len(campeonato) > 1):
        campeonato = Campeonato(id=id)
        campeonato = campeonato.delete_campeonato()

        if("error" in campeonato):
            return campeonato["error"], campeonato["status_code"]
        else:
            return campeonato
    else:
        return {"Erro" : "Campeonato não encontrado"}, 404

#Time
@app.route("/time", methods=["GET"])
def select_all_times():
    time = Team()
    time = time.select_all()

    if("error" in time):
        return time["error"], time["status_code"]
    else:
        return time

@app.route("/time/<int:id>", methods=["GET"])
def select_time(id):
    time = Team(id = id)
    time =  time.select_by_id()

    if("error" in time):
        return time["error"], time["status_code"]
    else:
        return time

@app.route("/time/select_oldest_team", methods=["GET"])
def select_oldest():
    time = Team()
    time =  time.select_oldest_team()

    if("error" in time):
        return time["error"], time["status_code"]
    else:
        return time

@app.route("/time/select_president_by_desc", methods=["GET"])
def select_desc_presidente():
    time = Team()
    time =  time.select_desc_presidente()

    if("error" in time):
        return time["error"], time["status_code"]
    else:
        return time

@app.route("/time/", methods=["POST"])
def add_time():
    identidade = verifica_identidade(request.headers)

    if("error" in identidade.keys()):
        return identidade["error"], identidade['status_code']

    if(identidade["result"]["is_editor"] != 1):
        return {"Erro": "Seu usuário não tem permissão para adicionar campeonatos"}, 401
    
    try:
        data = json.loads(request.data)
    except:
        return {"Erro": "Request inválida"}, 400

    if('nome' not in data.keys() or 'ano_fundacao' not in data.keys() or 'presidente' not in data.keys()):
        return {"Erro": "Dados faltando na request!"}, 400

    if(data['nome'] != "" and  data['nome'] != None and data['ano_fundacao'] != "" and data['ano_fundacao'] != None and data['presidente'] != "" and data["presidente"] != None):
        
        time = Team(nome=data['nome'], ano_fundacao=data['ano_fundacao'], presidente=data['presidente'], owner_username=identidade['result']["username"])
        time = time.add_time()

        if("error" in time):
            return time["error"], time["status_code"]
        else:
            return time

    else:
        return {"Erro": "Dados inválidos na request"}, 400



if __name__ == "__main__":
    app.run(debug=True)