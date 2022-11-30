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

    usuario = Usuario(login=auth['username'], password=auth['password'])

    usuario = usuario.select_usuario_by_login()

    if("Erro" in usuario.keys()):
        return usuario["Erro"], usuario["status_code"]
    else:
        if(len(usuario) > 1):
                
            expire_date = pendulum.now()
            
            expire_date = expire_date.add(minutes=5)

            usuario["expire_date"] = datetime.timestamp(expire_date)

            return {'token': jwt.encode(payload=usuario, key="projeto_rest"), 'expira_em': usuario["expire_date"]}
            
    return {"Erro": "Usuário ou senha não encontrados"}, 401

def is_autenticado(headers):
    auth = dict(headers)

    if('Authorization' not in auth.keys()):
        return {"Erro": "Token não informado"} , 400
    elif('Bearer' not in auth['Authorization']):
        return {"Erro": "Token não informado"} , 400
    else:
        auth = headers["Authorization"]

    auth = auth.split()

    try:
        auth = jwt.decode(auth[1], algorithms=['HS256'], key="projeto_rest")
    except DecodeError:
        return {"Erro": "Token informado não é valido"}, 401
    except:
        return {"Erro": "Token informado não é valido"}, 401


    

    return "teste"

@app.route("/usuario", methods=["POST"])
def add_user():
    print(is_autenticado(request.headers))

    return "teste"



@app.route("/campeonato/<int:id>", methods=["GET"])
def select_id(id):

    campeonato = Campeonato()

    return campeonato.select_by_id(id)


@app.route("/campeonato", methods=["GET"])
def select_all():

    campeonato = Campeonato()

    return campeonato.select_all()





'''
@app.route("/campeonato/select_by_name/<string:nome_campeonato>", methods=["GET"])
def select_by_name(nome_campeonato):

    campeonato = Campeonato(nome=nome_campeonato)

    return campeonato.select_by_name()

@app.route("/campeonato/select_top_premiacao")
def select_top_premiacao():
    campeonato = Campeonato()

    return campeonato.select_top_premiacao()

@app.route("/campeonato", methods=["POST"])
def add_campeonato():

    data = json.loads(request.data)

    if('nome' not in data.keys() or 'premiacao' not in data.keys()):
        return "Nome ou premiação não foi informado", 400

    if(data['nome'] != "" and data['premiacao'] != "" and data['nome'] != None and data['premiacao'] != None):
        
        campeonato = Campeonato(nome=data['nome'], premiacao=data['premiacao'], etapa=data.get('etapa', None))
        
        return campeonato.add_campeonato()
    
    else:
        return "Nome ou premiação está vazio", 400

@app.route("/campeonato/<int:id>", methods=["DELETE"])
def delete_campeonato(id):

    campeonato = Campeonato()

    return campeonato.delete_campeonato(id)

@app.route("/campeonato/<int:id>", methods=["PUT"])
def update_campeonato(id):
    try:
        data = json.loads(request.data)

        if('nome' not in data.keys() or 'premiacao' not in data.keys()):
            return {"Erro": "Nome ou premiação não foi informado"}, 400

        if(data['nome'] != "" and data['premiacao'] != "" and data['nome'] != None and data['premiacao'] != None):
            
            campeonato = Campeonato(nome=data['nome'], premiacao=data['premiacao'], etapa=data.get('etapa', None))
            
            return campeonato.update_campeonato(id)
        
        else:
            return {"Erro": "Nome ou premiação está vazio"}, 400
    except JSONDecodeError:
        return {"Erro": "Não foi informado nenhum objeto na request"}, 400

#Time


'''
if __name__ == "__main__":
    app.run(debug=True)