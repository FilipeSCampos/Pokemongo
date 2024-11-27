from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import Pokemon, Battle, Leaderboard
import random
from .utils import create_random_npc



def home(request):
    return render(request, 'home.html')


from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            return render(request, 'core/register.html', {'error': 'Usuário já existe!'})
        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        return redirect('home')
    return render(request, 'core/register.html')



def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'core/login.html', {'error': 'Usuário ou senha inválidos.'})
    return render(request, 'core/login.html')


def logout_view(request):
    logout(request)
    return redirect('home')


@login_required
def select_pokemon(request):
    pokemons = Pokemon.objects.all()
    if request.method == 'POST':
        selected_ids = request.POST.getlist('pokemon_ids')
        request.session['player_team'] = selected_ids
        return redirect('battle')
    return render(request, 'select_pokemon.html', {'pokemons': pokemons})


@login_required
def battle(request):
    player_team = [Pokemon.objects.get(id=p_id) for p_id in request.session.get('player_team')]
    npc = create_random_npc()
    npc_team = npc.pokemons

    # Simulação da batalha
    player_hp = sum(p.hp for p in player_team)
    npc_hp = sum(p.hp for p in npc_team)

    winner = 'Player' if player_hp > npc_hp else 'NPC'

    # Registrar batalha
    Battle.objects.create(
        player=request.user,
        player_team=[p.id for p in player_team],
        npc=npc,
        winner=winner
    )

    # Atualizar leaderboard
    if winner == 'Player':
        leaderboard = Leaderboard.objects.get(player=request.user)
        leaderboard.battles_won += 1
        leaderboard.save()

    return render(request, 'battle.html', {'player_team': player_team, 'npc_team': npc_team, 'winner': winner})


from django.shortcuts import render
from core.models import Leaderboard

def leaderboard_view(request):
    leaderboard = Leaderboard.objects.all().order_by('-battles_won')  # Ordenar por vitórias
    return render(request, "core/leaderboard.html", {"leaderboard": leaderboard})



from django.shortcuts import redirect

def start_battle(request):
    if not request.user.is_authenticated:
        return redirect('login')  # Redireciona para login se não estiver autenticado
    return redirect('choose_team')  # Redireciona para escolha de time

from django.shortcuts import render
from .models import Pokemon

def choose_team(request):
    if not request.user.is_authenticated:
        return redirect('login')  # Redireciona para login se não estiver autenticado

    pokemons = Pokemon.objects.all()
    return render(request, 'core/choose_team.html', {'pokemons': pokemons})

from django.shortcuts import render, redirect
from .models import Pokemon, NPC, Battle
from random import choice

from random import choice

from random import randint

def battle(request):
    if request.method == 'POST':
        selected_ids = request.POST.getlist('selected_pokemons')
        if len(selected_ids) != 3:
            return redirect('choose_team')  # Certifique-se de que o jogador selecionou 3 Pokémons

        # Obtenha os Pokémons escolhidos pelo jogador
        player_team = Pokemon.objects.filter(id__in=selected_ids)

        # Selecionar NPC aleatório
        npc = random.choice(NPC.objects.all())

        # Obtenha os Pokémons do NPC
        npc_team = npc.pokemons.all()

        # Calcular a pontuação do jogador
        player_score = sum([
            pokemon.attack + pokemon.defense + pokemon.hp
            for pokemon in player_team
        ]) + 20  # Bônus para o jogador

        # Calcular a pontuação do NPC
        npc_score = sum([
            pokemon.attack + pokemon.defense + pokemon.hp
            for pokemon in npc_team
        ])

        # Determinar o vencedor
        if player_score > npc_score:
            winner = 'player'
        elif player_score < npc_score:
            winner = 'npc'
        else:
            winner = 'player'  # Jogador vence em caso de empate

        # Registrar a batalha no banco de dados
        Battle.objects.create(
            player=request.user,
            player_team=[pokemon.id for pokemon in player_team],
            npc=npc,
            winner='Você' if winner == 'player' else npc.name
        )

        return render(request, 'core/battle_result.html', {
            'player_team': player_team,
            'npc_name': npc.name,
            'npc_team': npc_team,
            'winner': 'Você' if winner == 'player' else npc.name,
        })
    else:
        return redirect('choose_team')



# core/views.py

from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Battle, Pokemon, NPC
import random

def battle_view(request):
    if request.method == "POST":
        # Recebe os dados do ataque selecionado pelo jogador
        attack_id = int(request.POST.get("attack_id"))
        pokemon_id = int(request.POST.get("pokemon_id"))
        npc_pokemon_id = int(request.POST.get("npc_pokemon_id"))

        # Busca os objetos Pokémon
        player_pokemon = Pokemon.objects.get(id=pokemon_id)
        npc_pokemon = Pokemon.objects.get(id=npc_pokemon_id)

        # Simula o turno do jogador
        attack = next(
            attack for attack in player_pokemon.attacks if attack["id"] == attack_id
        )
        damage_to_npc = calculate_damage(attack, npc_pokemon.type)
        npc_pokemon.hp -= damage_to_npc

        # Checa se o NPC foi derrotado
        if npc_pokemon.hp <= 0:
            return JsonResponse({"status": "npc_defeated"})

        # Turno do NPC
        npc_attack = random.choice(npc_pokemon.attacks)
        damage_to_player = calculate_damage(npc_attack, player_pokemon.type)
        player_pokemon.hp -= damage_to_player

        # Checa se o jogador foi derrotado
        if player_pokemon.hp <= 0:
            return JsonResponse({"status": "player_defeated"})

        # Atualiza os HPs no banco de dados
        npc_pokemon.save()
        player_pokemon.save()

        return JsonResponse(
            {
                "status": "continue",
                "player_pokemon_hp": player_pokemon.hp,
                "npc_pokemon_hp": npc_pokemon.hp,
                "npc_attack": npc_attack,
            }
        )
    else:
        # Renderiza a página inicial da batalha
        player_team = request.session.get("player_team", [])
        if not player_team:
            return redirect("choose_team")

        npc = random.choice(NPC.objects.all())
        npc_pokemon = random.choice(npc.pokemons.all())

        player_pokemon = Pokemon.objects.get(id=player_team[0])  # Primeiro do time

        return render(
            request,
            "core/battle.html",
            {
                "player_pokemon": player_pokemon,
                "npc_pokemon": npc_pokemon,
                "player_team": player_team,
            },
        )


def calculate_damage(attack, target_type):
    # Dano básico
    base_damage = attack["power"]

    # Verifica se há vantagem de tipo
    strong_against = {
        "Fire": ["Grass", "Bug", "Ice", "Steel"],
        "Water": ["Fire", "Ground", "Rock"],
        "Grass": ['Water', 'Rock', 'Ground'],
        'Electric': ['Water', 'Flying'],
        'Ice': ['Grass', 'Ground', 'Flying', 'Dragon'],
        'Rock': ['Fire', 'Bug', 'Flying', 'Ice'],
        'Ground': ['Fire', 'Electric', 'Rock', 'Steel'],
        'Flying': ['Grass', 'Bug', 'Fighting'],
        'Bug':  ['Grass', 'Psychic', 'Dark'],
        'Psychic': ['Fighting', 'Poison'],
        'Dark':  ['Psychic', 'Ghost'],
        'Ghost':  ['Psychic', 'Ghost'],
        'Steel': ['Rock', 'Ice', 'Fairy'],
        'Fairy': ['Dark', 'Dragon', 'Fighting'],
        'Dragon': ['Dragon'],
    }

    if target_type in strong_against.get(attack["type"], []):
        base_damage *= 1.5  # Dano aumentado

    return int(base_damage)
