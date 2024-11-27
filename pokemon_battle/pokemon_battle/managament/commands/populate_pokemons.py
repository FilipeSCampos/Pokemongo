from django.core.management.base import BaseCommand
from core.data.populate_data import create_attacks, create_pokemons

class Command(BaseCommand):
    help = 'Popula o banco de dados com ataques, tipos e pokémons.'

    def handle(self, *args, **kwargs):
        self.stdout.write("Populando ataques...")
        create_attacks()
        self.stdout.write(self.style.SUCCESS("Ataques populados com sucesso!"))
        
        self.stdout.write("Populando pokémons...")
        create_pokemons()
        self.stdout.write(self.style.SUCCESS("Pokémons populados com sucesso!"))
