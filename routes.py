from flask import Flask, jsonify, render_template
from flask_caching import Cache

from api.pokemon_list import PokemonList

pokedex = Flask(__name__)
cache = Cache()
cache.init_app(pokedex, config={"CACHE_TYPE": "simple"})


@pokedex.route('/')
@pokedex.route('/<page>')
def pokemon_scroll(page=1):
    pokemon_list = PokemonList()
    pokemon = pokemon_list.generate(page_num=page)
    pokemon_limit = pokemon_list.page_limit
    return render_template(
        'index.html',
        pokemons=pokemon,
        page=int(page),
        prev_page=False if int(page) == 1 else True,
        next_page=False if len(pokemon) < pokemon_limit else True
    )


@pokedex.route('/pokemon/<id>')
def pokemon(id: int):
    return id