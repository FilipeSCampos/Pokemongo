import os
import sys
import django
from django.core.files import File

# Configuração do Django
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
sys.path.insert(0, BASE_DIR)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pokemon_battle.settings')
django.setup()

from core.models import Pokemon, NPC


def create_pokemons():
    """Cria todos os 15 Pokémons com ataques e imagens."""
    pokemons_data = [
        {
            'name': 'Charizard',
            'type': 'Fire',
            'hp': 360,
            'attack': 293,
            'defense': 280,
            'attacks': [
                {'name': 'Fire Blast', 'type': 'Fire', 'power': 120},
                {'name': 'Flamethrower', 'type': 'Fire', 'power': 90},
                {'name': 'Dragon Claw', 'type': 'Dragon', 'power': 80},
                {'name': 'Slash', 'type': 'Normal', 'power': 70},
            ],
            'image': 'charizard.png',
        },
        {
            'name': 'Blastoise',
            'type': 'Water',
            'hp': 362,
            'attack': 291,
            'defense': 328,
            'attacks': [
                {'name': 'Water Gun', 'type': 'Water', 'power': 50},
                {'name': 'Hydro Pump', 'type': 'Water', 'power': 110},
                {'name': 'Bite', 'type': 'Dark', 'power': 60},
                {'name': 'Ice Beam', 'type': 'Ice', 'power': 90},
            ],
            'image': 'blastoise.png',
        },
        {
            'name': 'Venusaur',
            'type': 'Grass',
            'hp': 364,
            'attack': 289,
            'defense': 291,
            'attacks': [
                {'name': 'Razor Leaf', 'type': 'Grass', 'power': 55},
                {'name': 'Solar Beam', 'type': 'Grass', 'power': 120},
                {'name': 'Sludge Bomb', 'type': 'Poison', 'power': 90},
                {'name': 'Earthquake', 'type': 'Ground', 'power': 100},
            ],
            'image': 'venusaur.png',
        },
        {
            'name': 'Pikachu',
            'type': 'Electric',
            'hp': 274,
            'attack': 229,
            'defense': 196,
            'attacks': [
                {'name': 'Thunderbolt', 'type': 'Electric', 'power': 90},
                {'name': 'Quick Attack', 'type': 'Normal', 'power': 40},
                {'name': 'Iron Tail', 'type': 'Steel', 'power': 100},
                {'name': 'Electro Ball', 'type': 'Electric', 'power': 80},
            ],
            'image': 'pikachu.png',
        },
        {
            'name': 'Lapras',
            'type': 'Ice',
            'hp': 384,
            'attack': 251,
            'defense': 297,
            'attacks': [
                {'name': 'Ice Beam', 'type': 'Ice', 'power': 90},
                {'name': 'Surf', 'type': 'Water', 'power': 90},
                {'name': 'Body Slam', 'type': 'Normal', 'power': 85},
                {'name': 'Hydro Pump', 'type': 'Water', 'power': 110},
            ],
            'image': 'lapras.png',
        },
        {
            'name': 'Gengar',
            'type': 'Ghost',
            'hp': 324,
            'attack': 261,
            'defense': 219,
            'attacks': [
                {'name': 'Shadow Ball', 'type': 'Ghost', 'power': 80},
                {'name': 'Dark Pulse', 'type': 'Dark', 'power': 80},
                {'name': 'Sludge Bomb', 'type': 'Poison', 'power': 90},
                {'name': 'Psychic', 'type': 'Psychic', 'power': 90},
            ],
            'image': 'gengar.png',
        },
        {
            'name': 'Jolteon',
            'type': 'Electric',
            'hp': 334,
            'attack': 251,
            'defense': 194,
            'attacks': [
                {'name': 'Thunderbolt', 'type': 'Electric', 'power': 90},
                {'name': 'Quick Attack', 'type': 'Normal', 'power': 40},
                {'name': 'Volt Switch', 'type': 'Electric', 'power': 70},
                {'name': 'Thunder Wave', 'type': 'Electric', 'power': 0},
            ],
            'image': 'jolteon.png',
        },
        {
            'name': 'Dragonite',
            'type': 'Dragon',
            'hp': 386,
            'attack': 319,
            'defense': 280,
            'attacks': [
                {'name': 'Dragon Claw', 'type': 'Dragon', 'power': 80},
                {'name': 'Hurricane', 'type': 'Flying', 'power': 110},
                {'name': 'Hyper Beam', 'type': 'Normal', 'power': 150},
                {'name': 'Earthquake', 'type': 'Ground', 'power': 100},
            ],
            'image': 'dragonite.png',
        },
        {
            'name': 'Snorlax',
            'type': 'Normal',
            'hp': 524,
            'attack': 250,
            'defense': 250,
            'attacks': [
                {'name': 'Rock Slide', 'type': 'Rock', 'power': 75},
                {'name': 'Body Slam', 'type': 'Normal', 'power': 85},
                {'name': 'Rest', 'type': 'Psychic', 'power': 0},
                {'name': 'Hyper Beam', 'type': 'Normal', 'power': 150},
            ],
            'image': 'snorlax.png',
        },
        {
            'name': 'Machamp',
            'type': 'Fighting',
            'hp': 384,
            'attack': 328,
            'defense': 282,
            'attacks': [
                {'name': 'Dynamic Punch', 'type': 'Fighting', 'power': 100},
                {'name': 'Karate Chop', 'type': 'Fighting', 'power': 50},
                {'name': 'Earthquake', 'type': 'Ground', 'power': 100},
                {'name': 'Cross Chop', 'type': 'Fighting', 'power': 100},
            ],
            'image': 'machamp.png',
        },
         {
        'name': 'Alakazam',
        'type': 'Psychic',
        'hp': 314,
        'attack': 271,
        'defense': 180,
        'attacks': [
            {'name': 'Psychic', 'type': 'Psychic', 'power': 90},
            {'name': 'Shadow Ball', 'type': 'Ghost', 'power': 80},
            {'name': 'Dazzling Gleam', 'type': 'Fairy', 'power': 80},
            {'name': 'Energy Ball', 'type': 'Grass', 'power': 90},
        ],
        'image': 'alakazam.png',
        },
        {
            'name': 'Steelix',
            'type': 'Steel',
            'hp': 354,
            'attack': 251,
            'defense': 398,
            'attacks': [
                {'name': 'Iron Tail', 'type': 'Steel', 'power': 100},
                {'name': 'Earthquake', 'type': 'Ground', 'power': 100},
                {'name': 'Rock Slide', 'type': 'Rock', 'power': 75},
                {'name': 'Crunch', 'type': 'Dark', 'power': 80},
            ],
            'image': 'steelix.png',
        },
        {
            'name': 'Sylveon',
            'type': 'Fairy',
            'hp': 334,
            'attack': 251,
            'defense': 280,
            'attacks': [
                {'name': 'Moonblast', 'type': 'Fairy', 'power': 95},
                {'name': 'Psychic', 'type': 'Psychic', 'power': 90},
                {'name': 'Shadow Ball', 'type': 'Ghost', 'power': 80},
                {'name': 'Hyper Voice', 'type': 'Normal', 'power': 90},
            ],
            'image': 'sylveon.png',
        },
        {
            'name': 'Tyranitar',
            'type': 'Rock',
            'hp': 404,
            'attack': 314,
            'defense': 288,
            'attacks': [
                {'name': 'Rock Slide', 'type': 'Rock', 'power': 75},
                {'name': 'Crunch', 'type': 'Dark', 'power': 80},
                {'name': 'Earthquake', 'type': 'Ground', 'power': 100},
                {'name': 'Stone Edge', 'type': 'Rock', 'power': 100},
            ],
            'image': 'tyranitar.png',
        },
        {
            'name': 'Gyarados',
            'type': 'Water',
            'hp': 394,
            'attack': 319,
            'defense': 247,
            'attacks': [
                {'name': 'Waterfall', 'type': 'Water', 'power': 80},
                {'name': 'Crunch', 'type': 'Dark', 'power': 80},
                {'name': 'Ice Fang', 'type': 'Ice', 'power': 65},
                {'name': 'Earthquake', 'type': 'Ground', 'power': 100},
            ],
            'image': 'gyarados.png',
    },
        
    ]

    for pokemon_data in pokemons_data:
        attacks = pokemon_data.pop('attacks', [])  # Extraímos os ataques com valor padrão de lista vazia
        if not isinstance(attacks, list):  # Validação extra
            print(f"Ataques inválidos para {pokemon_data['name']}: {attacks}")
            continue

        # Garantir que o campo não seja None ou vazio
        pokemon_data['attacks'] = attacks if attacks else []

        image_path = pokemon_data.pop('image', None)

        # Cria o Pokémon
        pokemon = Pokemon.objects.create(**pokemon_data)

        # Salva a imagem no campo image
        if image_path:
            image_full_path = os.path.join('pokemon_battle\core\static\core\images', image_path)
            if os.path.exists(image_full_path):
                with open(image_full_path, 'rb') as img_file:
                    pokemon.image.save(image_path, File(img_file))
                    print(f"Imagem carregada para: {pokemon.name}")
            else:
                print(f"Imagem não encontrada para: {pokemon.name}")


def create_npcs():
    """Cria NPCs e associa Pokémons a eles."""
    npcs_data = [
        {
            'name': 'NPC Trainer Red',
            'pokemons': ['Charizard', 'Blastoise', 'Venusaur'],
        },
        {
            'name': 'NPC Trainer Blue',
            'pokemons': ['Pikachu', 'Lapras', 'Dragonite'],
        },
        {
            'name': 'NPC Trainer Green',
            'pokemons': ['Gengar', 'Jolteon', 'Snorlax'],
        },
    ]

    for npc_data in npcs_data:
        npc = NPC.objects.create(name=npc_data['name'])
        for pokemon_name in npc_data['pokemons']:
            pokemon = Pokemon.objects.filter(name=pokemon_name).first()
            if pokemon:
                npc.pokemons.add(pokemon)
        npc.save()
        print(f"NPC criado: {npc.name}")


def main():
    print("Populando Pokémons...")
    create_pokemons()
    print("Pokémons populados com sucesso!")

    print("Populando NPCs...")
    create_npcs()
    print("NPCs populados com sucesso!")


if __name__ == "__main__":
    main()
