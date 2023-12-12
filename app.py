from flask import Flask, render_template
import requests

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped,mapped_column


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///pokedex.sqlite"

db = SQLAlchemy(app)


class Pokedex (db.Model):
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True,autoincrement=True)
    name: Mapped[str] = mapped_column(db.String, nullable=False)

with app.app_context():
    db.create_all()

def get_pokemon_data(pokemon):
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon}'
    r = requests.get(url).json()
    return r        

@app.route("/")
def home():
    return render_template('pokemon.html')

@app.route("/detalle")
def detalle():
    return render_template('detalle.html')



#PRUEBA
@app.route("/insert")
def insert():
    new_pokemon = 'charmander'
    if new_pokemon:
        obj=Pokedex(name=new_pokemon)
        db.session.add(obj)
        db.session.commit()
    return 'pokemon agregado'


@app.route("/select")
def select():
    lista_pokemon=Pokedex.query.all()
    return lista_pokemon


if __name__ == '__main__':
    app.run(debug=True)

