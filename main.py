from pokemon import *
import requests

try:
    print('\033[1;32mBem Vindo ao Verificador de Pokemons :D\033[m')
    pokemon = input(f'Digite seu Pokemon: ').lower()
    api = f'https://pokeapi.co/api/v2/pokemon/{pokemon}'
    re = requests.get(api)
    poke_json = re.json()
    pokemon_objeto = Pokemon(poke_json)
    print()
    pokemon_objeto.listar_ataques()
    print()
    pokemon_objeto.listar_movimentos()
    print()
    pokemon_objeto.listar_status()
except AssertionError as erro:
    print(erro)
except:
    print('Ocorreu um erro fatal :c')