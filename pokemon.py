class Pokemon:
    def __init__(self, pokemon):
        self.pokemon = pokemon

    @property
    def pokemon(self):
        return self.__pokemon

    @pokemon.setter
    def pokemon(self, pokemon):
        assert type(pokemon) == dict, "O argumento deve ser o json do request do seu Pokemon"
        self.__pokemon = pokemon

    def listar_ataques(self):
        habilidades = ', '.join([str(i['ability']['name'].capitalize()) for i in self.pokemon['abilities']])
        print(f'\033[1;31mAbilities:\033[m \n{habilidades}')

    def listar_movimentos(self):
        movimentos = ', '.join([str(i['move']['name'].capitalize()) for i in self.pokemon['moves']])
        print(f'\033[1;31mMoves:\033[m \n{movimentos}')


    def listar_status(self):
        print('\033[1;31mStatus:\033[m ')
        for i in self.pokemon['stats']:
            print(f"{i['stat']['name'].capitalize()} = {i['base_stat']}")
        for i in self.pokemon['types']:
            print(f"Type: {i['type']['name'].capitalize()}")
        print(f"Height: {self.pokemon['height']}m")
        print(f"Weight: {self.pokemon['weight']}kg")
    