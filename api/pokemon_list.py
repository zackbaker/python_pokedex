from models.pokemon import Pokemon


class PokemonList:
    def __init__(self):
        self.page_limit = 8
        self.last_pokemon_id = 151

    def generate(self, page_num):
        pokemon_list = []

        for i in range(1, self.page_limit + 1):
            multiplier = int(page_num) - 1
            pokemon = i + (multiplier * self.page_limit)
            pokemon_list.append(Pokemon().set_pokemon(pokemon))

            if pokemon == self.last_pokemon_id:
                break

        return pokemon_list
