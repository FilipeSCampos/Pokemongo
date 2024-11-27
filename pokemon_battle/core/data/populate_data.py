# core/data/populate_data.py

from core.models import Attack, Pokemon
from core.data.pokemon_types import pokemon_types
import os
from django.core.files import File

def validate_type(type_name):
    """Valida se o tipo existe no dicionário pokemon_types."""
    if type_name not in pokemon_types:
        raise ValueError(f"Tipo inválido: {type_name}")

def create_attacks():
    attacks = [
        {'name': 'Fire Blast', 'type': 'Fire', 'power': 120},
        {'name': 'Water Gun', 'type': 'Water', 'power': 50},
        {'name': 'Razor Leaf', 'type': 'Grass', 'power': 55},
        {'name': 'Thunderbolt', 'type': 'Electric', 'power': 90},
        {'name': 'Ice Beam', 'type': 'Ice', 'power': 90},
        {'name': 'Rock Slide', 'type': 'Rock', 'power': 75},
        {'name': 'Earthquake', 'type': 'Ground', 'power': 100},
        {'name': 'Psychic', 'type': 'Psychic', 'power': 90},
        {'name': 'Shadow Ball', 'type': 'Ghost', 'power': 80},
        {'name': 'Iron Tail', 'type': 'Steel', 'power': 100},
        {'name': 'Moonblast', 'type': 'Fairy', 'power': 95},
    ]
    
    attack_objects = []
    for attack in attacks:
        validate_type(attack['type'])  # Valida o tipo do ataque
        attack_obj = Attack.objects.create(**attack)
        attack_objects.append(attack_obj)
    return attack_objects


def create_pokemons():
    # Diretório das imagens
    base_path = os.path.join('core', 'static', 'core', 'images')
    
    # Dados dos Pokémons
    pokemons = [
        {
            'name': 'Charizard',
            'type': 'Fire',
            'hp': 360,
            'attack': 293,
            'defense': 280,
            'attacks': [{'name': 'Fire Blast', 'type': 'Fire', 'power': 120}],
            'image': 'charizard.png'
        },
        {
            'name': 'Blastoise',
            'type': 'Water',
            'hp': 362,
            'attack': 291,
            'defense': 328,
            'attacks': [{'name': 'Water Gun', 'type': 'Water', 'power': 50}],
            'image': 'blastoise.png'
        },
        {
            'name': 'Venusaur',
            'type': 'Grass',
            'hp': 364,
            'attack': 289,
            'defense': 291,
            'attacks': [{'name': 'Razor Leaf', 'type': 'Grass', 'power': 55}],
            'image': 'venusaur.png'
        },
        {
            'name': 'Pikachu',
            'type': 'Electric',
            'hp': 274,
            'attack': 229,
            'defense': 196,
            'attacks': [{'name': 'Thunderbolt', 'type': 'Electric', 'power': 90}],
            'image': 'pikachu.png'
        },
        {
            'name': 'Lapras',
            'type': 'Ice',
            'hp': 384,
            'attack': 251,
            'defense': 297,
            'attacks': [{'name': 'Ice Beam', 'type': 'Ice', 'power': 90}],
            'image': 'lapras.png'
        },
        {
            'name': 'Gengar',
            'type': 'Ghost',
            'hp': 324,
            'attack': 261,
            'defense': 219,
            'attacks': [{'name': 'Shadow Ball', 'type': 'Ghost', 'power': 80}],
            'image': 'gengar.png'
        },
        {
            'name': 'Jolteon',
            'type': 'Electric',
            'hp': 334,
            'attack': 251,
            'defense': 194,
            'attacks': [{'name': 'Thunderbolt', 'type': 'Electric', 'power': 90}],
            'image': 'jolteon.png'
        },
        {
            'name': 'Dragonite',
            'type': 'Dragon',
            'hp': 386,
            'attack': 319,
            'defense': 280,
            'attacks': [{'name': 'Earthquake', 'type': 'Ground', 'power': 100}],
            'image': 'dragonite.png'
        },
        {
            'name': 'Snorlax',
            'type': 'Normal',
            'hp': 524,
            'attack': 250,
            'defense': 250,
            'attacks': [{'name': 'Rock Slide', 'type': 'Rock', 'power': 75}],
            'image': 'snorlax.png'
        },
        {
            'name': 'Machamp',
            'type': 'Fighting',
            'hp': 384,
            'attack': 328,
            'defense': 282,
            'attacks': [{'name': 'Rock Slide', 'type': 'Rock', 'power': 75}],
            'image': 'machamp.png'
        },
        {
            'name': 'Sylveon',
            'type': 'Fairy',
            'hp': 334,
            'attack': 251,
            'defense': 280,
            'attacks': [{'name': 'Moonblast', 'type': 'Fairy', 'power': 95}],
            'image': 'sylveon.png'
        },
        {
            'name': 'Steelix',
            'type': 'Steel',
            'hp': 354,
            'attack': 251,
            'defense': 398,
            'attacks': [{'name': 'Iron Tail', 'type': 'Steel', 'power': 100}],
            'image': 'steelix.png'
        },
        {
            'name': 'Tyranitar',
            'type': 'Rock',
            'hp': 404,
            'attack': 314,
            'defense': 288,
            'attacks': [{'name': 'Rock Slide', 'type': 'Rock', 'power': 75}],
            'image': 'tyranitar.png'
        },
        {
            'name': 'Alakazam',
            'type': 'Psychic',
            'hp': 314,
            'attack': 271,
            'defense': 180,
            'attacks': [{'name': 'Psychic', 'type': 'Psychic', 'power': 90}],
            'image': 'alakazam.png'
        },
        {
            'name': 'Gyarados',
            'type': 'Water',
            'hp': 394,
            'attack': 319,
            'defense': 247,
            'attacks': [{'name': 'Water Gun', 'type': 'Water', 'power': 50}],
            'image': 'gyarados.png'
        }
    ]
    
    for pokemon_data in pokemons:
        validate_type(pokemon_data['type'])  # Valida o tipo do Pokémon
        attacks = pokemon_data.pop('attacks')
        image_path = pokemon_data.pop('image')
        pokemon = Pokemon.objects.create(**pokemon_data)
        for attack in attacks:
            validate_type(attack['type'])  # Valida o tipo do ataque
            attack_obj, _ = Attack.objects.get_or_create(**attack)
            pokemon.attacks.append(attack_obj)
        pokemon.save()
        # Salva a imagem no campo 'image'
        with open(os.path.join(base_path, image_path), 'rb') as img_file:
            pokemon.image.save(image_path, File(img_file))
