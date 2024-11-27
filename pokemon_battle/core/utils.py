# core/utils.py
import random
from .models import NPC, Pokemon

def create_random_npc():
    pokemons = random.sample(list(Pokemon.objects.all()), 3)  # Seleciona 3 pokémons aleatórios
    npc = NPC.objects.create(name=f'NPC {random.randint(1, 1000)}', pokemons=pokemons)
    return npc


# core/utils.py
from core.data.pokemon_types import pokemon_types

def calculate_damage(attacker, defender, attack):
    damage = attack.power + (attacker.attack - defender.defense)
    type_modifiers = pokemon_types[attack.type]
    if defender.type in type_modifiers['strong_against']:
        damage *= 2
    elif defender.type in type_modifiers['weak_against']:
        damage /= 2
    return max(1, int(damage))  # Garante que o dano mínimo seja 1
