class Player:
    def __init__(self,name):
        self.name = name
        self.level = 1
        self.xp = 0
        self.xp_to_level = 100

        self.strength = 10
        self.agility = 10
        self.intelligence = 10

    def status(self):
        print(f"Nome: {self.name}")
        print(f"Nivel: {self.level}")
        print(f"XP:{self.xp}")
        print(f"Força: {self.strength}")
        print(f"Agilidade: {self.agility}")
        print(f"Inteligencia: {self.intelligence}")
        print("_" * 30)

    def gain_xp(self, amount):
        print(f"ganhou {amount} de XP")
        self.xp += amount

        if self.xp >= self.xp_to_level:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.xp -= self.xp_to_level
        self.xp_to_level += 50

        self.strength += 2
        self.agility += 2
        self.intelligence += 2

        print("LEVEL UP")
        print(f"Agora você é nível {self.level}")


player = Player("Caçador")
print("Sistema Solo Leveling iniciado\n")

player.status()
player.gain_xp(120)
player.status()