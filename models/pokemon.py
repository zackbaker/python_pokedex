from math import floor

from connectors.pokeapi import Pokeapi


class Pokemon:
    def __init__(self):
        self.id = 0
        self.name = ''
        self.sprite = ''
        self.abilities = []
        self.weight = 0
        self.height = 0
        self.types = []
        self.stats = []
        self.moves = []

    def set_pokemon(self, pokemon):
        pokeapi = Pokeapi()
        pokemon_json = pokeapi.get_pokemon(pokemon)
        self.id = pokemon_json['id']
        self.name = pokemon_json['name'].capitalize()
        self.sprite = self.find_sprite(pokemon_json['sprites'])
        self.abilities = self.find_abilities(pokemon_json['abilities'])
        self.weight = self.find_weight(pokemon_json['weight'])
        self.height = self.find_height(pokemon_json['height'])
        self.types = self.find_types(pokemon_json['types'])
        self.stats = self.find_stats(pokemon_json['stats'])
        self.moves = self.find_moves(pokemon_json['moves'])
        return self

    def find_sprite(self, sprites):
        sprite = None

        for sprite, url in sprites.items():
            if 'front' in sprite and url is not None:
                sprite = url
                break

        if sprite is None:
            for sprite, url in sprites.items():
                if url is not None:
                    sprite = url

        return sprite

    def find_abilities(self, abillities):
        abilities_list = []

        for ability in abillities:
            abilities_list.append(ability['ability']['name'])

        return abilities_list

    def find_weight(self, weight):
        if weight > 4.54:
            return str(round(weight / 4.54)) + ' lbs'
        else:
            return str(round(weight / 100)) + ' grams'

    def find_height(self, height):
        inches = round(height / .254)

        if inches > 12:
            feet = floor(inches / 12)
            inches = inches - (feet * 12)
            return str(feet) + ' feet and ' + str(inches) + ' inches'
        else:
            return str(inches) + ' inches'

    def find_types(self, types):
        types_list = []

        for type in types:
            types_list.append(type['type']['name'])

        return types_list

    def find_stats(self, stats):
        stats_list = []

        for stat in stats:
            stats_list.append({'name': stat['stat']['name'], 'base_stat': stat['base_stat']})

        return stats_list

    def find_moves(self, moves):
        moves_list = []

        for move in moves:
            moves_list.append({
                'name': move['move']['name'],
                'level_learned_at': move['version_group_details'][0]['level_learned_at'],
                'learned_by': move['version_group_details'][0]['move_learn_method']['name']}
            )

        return sorted(moves_list, key=lambda move: move['level_learned_at'])
