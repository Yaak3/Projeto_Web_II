from flask import Flask
from flask import request
from team import Team
from campeonato import Campeonato
import json

app = Flask(__name__)

@app.route("/campeonato/<int:id>", methods=["GET"])
def select_id(id):

    campeonato = Campeonato()

    return campeonato.select_by_id(id)
    
@app.route("/campeonato", methods=["GET"])
def select_all():

    campeonato = Campeonato()

    return campeonato.select_all()


@app.route("/campeonato/select_by_name/<string:nome_campeonato>", methods=["GET"])
def select_by_name(nome_campeonato):

    campeonato = Campeonato(nome=nome_campeonato)

    return campeonato.select_by_name(), 200

@app.route("/campeonato/select_top_premiacao")
def select_top_premiacao():
    campeonato = Campeonato()

    return campeonato.select_top_premiacao(), 200



@app.route("/campeonato", methods=["POST"])
def add_campeonato():

    data = json.loads(request.data)

    if('nome' not in data.keys() or 'premiacao' not in data.keys()):
        return "Nome ou premiação não foi informado", 400

    if(data['nome'] != "" and data['premiacao'] != "" and data['nome'] != None and data['premiacao'] != None):
        
        campeonato = Campeonato(nome=data['nome'], premiacao=data['premiacao'], etapa=data.get('etapa', None))
        
        return campeonato.add_campeonato(), 200
    
    else:
        return "Nome ou premiação está vazio", 400

@app.route("/campeonato/<int:id>", methods=["DELETE"])
def delete_campeoato(id):

    campeonato = Campeonato()

    return campeonato.delete_campeoato(id)


if __name__ == "__main__":
    app.run(debug=True)