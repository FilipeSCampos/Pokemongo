pokemon_types = {
    'Fire': {'strong_against': ['Grass', 'Bug', 'Ice', 'Steel'], 'weak_against': ['Water', 'Rock', 'Fire', 'Dragon']},
    'Water': {'strong_against': ['Fire', 'Rock', 'Ground'], 'weak_against': ['Water', 'Grass', 'Dragon']},
    'Grass': {'strong_against': ['Water', 'Rock', 'Ground'], 'weak_against': ['Fire', 'Bug', 'Flying', 'Poison']},
    'Electric': {'strong_against': ['Water', 'Flying'], 'weak_against': ['Electric', 'Ground', 'Dragon']},
    'Ice': {'strong_against': ['Grass', 'Ground', 'Flying', 'Dragon'], 'weak_against': ['Fire', 'Water', 'Ice', 'Steel']},
    'Rock': {'strong_against': ['Fire', 'Bug', 'Flying', 'Ice'], 'weak_against': ['Water', 'Grass', 'Fighting', 'Ground']},
    'Ground': {'strong_against': ['Fire', 'Electric', 'Rock', 'Steel'], 'weak_against': ['Water', 'Grass', 'Ice']},
    'Flying': {'strong_against': ['Grass', 'Bug', 'Fighting'], 'weak_against': ['Electric', 'Rock', 'Ice']},
    'Bug': {'strong_against': ['Grass', 'Psychic', 'Dark'], 'weak_against': ['Fire', 'Flying', 'Rock']},
    'Psychic': {'strong_against': ['Fighting', 'Poison'], 'weak_against': ['Bug', 'Ghost', 'Dark']},
    'Dark': {'strong_against': ['Psychic', 'Ghost'], 'weak_against': ['Fighting', 'Bug', 'Fairy']},
    'Ghost': {'strong_against': ['Psychic', 'Ghost'], 'weak_against': ['Dark']},
    'Steel': {'strong_against': ['Rock', 'Ice', 'Fairy'], 'weak_against': ['Fire', 'Fighting', 'Ground']},
    'Fairy': {'strong_against': ['Dark', 'Dragon', 'Fighting'], 'weak_against': ['Steel', 'Poison']},
    'Dragon': {'strong_against': ['Dragon'], 'weak_against': ['Ice', 'Fairy']},
}
