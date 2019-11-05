from flask import Flask
from flask_caching import Cache

pokedex = Flask(__name__)
cache = Cache()
cache.init_app(pokedex)


@pokedex.route('/')
def pokemon_list():
    return 'Hello World!!!'
