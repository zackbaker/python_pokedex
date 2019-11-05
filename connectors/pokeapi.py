import requests


class Pokeapi:
    def __init__(self):
        self.pokeapi_url: str = 'https://pokeapi.co/api/v2/'

    def get_pokemon(self, pokemon):
        return requests.get(self.pokeapi_url + '/pokemon/' + str(pokemon)).json()
