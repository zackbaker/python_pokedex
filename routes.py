from flask import Flask, render_template
from flask_caching import Cache

from api.pokemon_view import PokemonView
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


@pokedex.route('/pokemon/<id>/<page_from>')
def pokemon(id, page_from):
    return render_template(
        'pokemon.html',
        pokemon=PokemonView().get_pokemon(id),
        return_page=page_from
    )


@pokedex.route('/search/<pokemon_search>')
def search(pokemon_search):
    pokemon = [PokemonView().get_pokemon(pokemon_search)]

    if pokemon[0] is not None:
        return render_template(
            'index.html',
            pokemons=pokemon,
            prev_page=False,
            next_pate=False
        )
    else:
        return render_template(
            'index.html',
            prev_page=False,
            next_pate=False
        )