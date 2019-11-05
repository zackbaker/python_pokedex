from models.pokemon import Pokemon


class PokemonList:
    def __init__(self):
        self.page_limit = 20
        self.page_limit = 8

    def generate(self, page_num: int):
        pokemon_list = []

        for i in range(1, self.page_limit + 1):
            pokemon_list.append(Pokemon().set_pokemon(i * page_num))

        return pokemon_list
