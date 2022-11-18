from flask import Flask
from flask import request
from campeonato import Campeonato
from time import Time
import json

app = Flask(__name__)

#Selects
@app.route("/campeonato/<id>", methods=["GET"])
def select_id(id):

    try:
        id = int(id)
        campeonato = Campeonato()
        return campeonato.select_by_id(id), 200
    except:
        return "Necessário informar um tipo inteiro como parâmetro", 400
    
@app.route("/campeonato", methods=["GET"])
def select_all():

    campeonato = Campeonato()

    return campeonato.select_all(), 200


@app.route("/campeonato/select_by_name/<nome>")
def select_by_name(nome):

    campeonato = Campeonato(nome=nome)

    return campeonato.select_by_name(), 200

@app.route("/campeonato/top_premiacao/")
def select_by_name():
    campeonato = Campeonato()

    return campeonato.select_top_premiacao(), 200


@app.route("/time/<id>", methods=["GET"])
def select_id(id):

    try:
        id = int(id)
        time = Time()
        return time.select_by_id(id), 200
    except:
        return "Necessário informar um tipo inteiro como parâmetro", 400
    
@app.route("/campeonato", methods=["GET"])
def select_all():

    time = Time()

    return time.select_all(), 200


@app.route("/campeonato/select_by_name/<nome>")
def select_by_name(nome):

    time = Time(nome=nome)

    return time.select_by_name(), 200

@app.route("/campeonato/select_oldest_team/")
def select_oldest_team():
    time = Time()

    return time.select_top_premiacao(), 200




@app.route("/campeonato", methods=["POST"])
def add_campeonato():

    data = json.loads(request.data)

    if('nome' not in data.keys() or 'premiacao' not in data.keys()):
        return "Error", 400
    
    campeonato = Campeonato(nome=data['nome'], premiacao=data['premiacao'], etapa=data.get('etapa', None))
    
    campeonato.add_campeonato()

    return "teste", 200

    


if __name__ == "__main__":
    app.run(debug=True)