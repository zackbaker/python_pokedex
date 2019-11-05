from flask import Flask, jsonify, render_template
from flask_caching import Cache

from api.pokemon_list import PokemonList

pokedex = Flask(__name__)
cache = Cache()
cache.init_app(pokedex, config={"CACHE_TYPE": "simple"})


@pokedex.route('/')
# @cache.cached(timeout=)
def pokemon_list():
    pokemon = PokemonList().generate(page_num=1)
    return render_template('index.html', pokemons=pokemon)

@pokedex.route('/pokemon/<id>')
def pokemon(id: int):
    return id