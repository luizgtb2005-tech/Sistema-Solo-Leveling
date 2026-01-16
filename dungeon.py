import random
from models import Enemy

class Dungeon:
    def __init__(self, name, enemies=None, has_chest=False):
        self.name = name
        self.enemies = enemies if enemies else[]
        self.has_chest = has_chest
        self.chest_items =[]

    def setup(self):
        """inicializa os inimigos e o baú se necessário"""
        if not self.enemies:
            self.enemies = [Enemy("Goblin", 50, 8), Enemy("Slime", 40, 5)]

        if self.has_chest:
            possible_items = ["poção", "força", "inteligencia"]
            self.chest_items = random.sample(possible_items, k=3)

    def enter(self, player):
        """Player entra na dungeon"""
        self.setup()
        print(f"\n🎯 {player.name} entrou na dungeon {self.name}!")

    def open_chest(self, player):
        """Abre o baú e adiciona itens ao inventario do player"""
        if not self.has_chest or not self.chest_items:
            print("Não ha baú para abrir nessa dungeon!")
            return

        print("\n🎁 Você encontrou um baú! itens adicionados ao inventario:")
        for item in self.chest_items:
            print(f"- {item}")
            player.inventory.append(item)

        # Esvazia o baú
        self.chest_items = []
        self.has_chest = False