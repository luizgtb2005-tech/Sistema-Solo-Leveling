class Player:
    def __init__(self, name):
        self.name = name
        self.max_hp = 100
        self.hp = self.max_hp
        self.level = 1
        self.xp = 0
        self.xp_to_level = 100
        self.points = 0
        self.inventory = []

        self.strength = 10
        self.agility = 10
        self.intelligence = 10

    def attack(self):
        return self.strength * 2

    def gain_xp(self, amount):
        self.xp += amount
        leveled = False

        while self.xp >= self.xp_to_level:
            self.xp -= self.xp_to_level
            self.level += 1
            self.points += 3
            self.xp_to_level += 50
            leveled = True

        return leveled

    def status(self):
        print(f"\n--- STATUS DO JOGADOR ---")
        print(f"Nome: {self.name}")
        print(f"HP: {self.hp}/{self.max_hp}")
        print(f"Nível: {self.level} XP: {self.xp}/{self.xp_to_level}")
        print(f"Pontos livres: {self.points}")
        print(f"Força: {self.strength} Agilidade: {self.agility} Inteligência: {self.intelligence}")

class Enemy:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack

    def is_alive(self):
        return self.hp > 0

ITEMS = {
    "poção": {"type": "heal", "value": 30},
    "força": {"type": "buff", "stat": "strength", "value": 2},
    "inteligencia": {"type": "buff", "stat": "intelligence", "value": 2}
}

def use_item(player, item_name):
    item = ITEMS[item_name]

    if item["type"] == "heal":
        player.hp = min(player.max_hp, player.hp + item["value"])

    elif item["type"] == "buff":
        setattr(player, item["stat"], getattr(player, item["stat"]) + item["value"])