from flask import Flask
from flask import request
from campeonato import Campeonato
import json

app = Flask(__name__)


@app.route("/campeonato/<id>", methods=["GET"])
def select_id(id):

    campeonato = Campeonato()

    return campeonato.select_by_id(id)

@app.route("/campeonato", methods=["GET"])
def select_all():

    campeonato = Campeonato()

    return campeonato.select_all()

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