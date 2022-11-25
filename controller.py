from flask import Flask
from flask import request
from team import Team
from campeonato import Campeonato
from usuario import Usuario
import json
from json import JSONDecodeError
from random import randint

app = Flask(__name__)

@app.route("/usuario/<int:id>", methods=["GET"])
def select_usuario(id):

    usuario = Usuario()

    return usuario.select_usuario(id)

@app.route("/usuario", methods=["GET"])
def login_user():
    auth = request.authorization
    try:
        auth = request.authorization
        print(app.config.get('SECRET_KEY'))
        return "teste"
    except:
        return {"erro": "login ou senha não informados no cabeçalho"}, 400








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