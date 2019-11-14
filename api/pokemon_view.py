from models.pokemon import Pokemon


class PokemonView:
    def get_pokemon(self, id):
        return Pokemon().set_pokemon(id)
