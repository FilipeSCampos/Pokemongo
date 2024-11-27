from django.contrib.auth.models import User
from djongo import models


class Attack(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=20)
    power = models.IntegerField()

    class Meta:
        abstract = True  # Indica que este é um subdocumento e não uma tabela separada.

    def __str__(self):
        return f"{self.name} ({self.type}, {self.power})"


class Pokemon(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=20)
    hp = models.IntegerField()
    attack = models.IntegerField()
    defense = models.IntegerField()
    # Alterado para JSONField
    attacks = models.JSONField()  # Lista de ataques no formato JSON
    image = models.ImageField(upload_to='pokemon_images/', blank=True, null=True)

    def __str__(self):
        return self.name


class NPC(models.Model):
    name = models.CharField(max_length=50)
    pokemons = models.ManyToManyField(Pokemon)  # Relacionamento direto com os Pokémons

    def __str__(self):
        return self.name


class Battle(models.Model):
    player = models.ForeignKey(User, on_delete=models.CASCADE)
    player_team = models.JSONField()  # IDs dos Pokémons do jogador
    npc = models.ForeignKey(NPC, on_delete=models.CASCADE)
    winner = models.CharField(max_length=50)

    def __str__(self):
        return f"Battle: {self.player.username} vs {self.npc.name}"


class Leaderboard(models.Model):
    player = models.OneToOneField(User, on_delete=models.CASCADE)
    battles_won = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.player.username} - {self.battles_won} wins"
