class Player:
    def __init__(self,name):
        self.name = name
        self.level = 1
        self.xp = 0
        self.xp_to_level = 100
        self.points = 0

        self.strength = 10
        self.agility = 10
        self.intelligence = 10

    def status(self):
        print("\n--- STATUS DO JOGADOR: ---")
        print(f"Nome: {self.name}")
        print(f"Nivel: {self.level}")
        print(f"XP:{self.xp}/{self.xp_to_level}")
        print(f"Pontos livres: {self.points}")
        print(f"Força: {self.strength}")
        print(f"Agilidade: {self.agility}")
        print(f"Inteligencia: {self.intelligence}")
        print("--------------------------")

    def gain_xp(self, amount):
        print(f"\nGanhou {amount} de XP")
        self.xp += amount

        while self.xp >= self.xp_to_level:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.xp -= self.xp_to_level
        self.xp_to_level += 50
        self.points += 3

        print("\n🔥 LEVEL UP!")
        print(f"Agora você é nível {self.level}")
        print("Você ganhou 3 pontos de atributo")

    def distribute_points(self):
        while self.points > 0:
            print("\nEscolha um atributo para aumentar:")
            print("1 - Força")
            print("2 - Agilidade")
            print("3 - Inteligência")

            choise = input("Digite o número:")

            if choise == "1":
                self.strength += 1
            elif choise == "2":
                self.agility += 1
            elif choise == "3":
                self.intelligence += 1
            else:
                print("Escolha inválida")
                continue

            self.points -= 1
            print("Ponto distribuído!")

class Quest:
    def __init__(self, name, reward_xp):
        self.name = name
        self.reward_xp = reward_xp

    def complete(self, player):
        print(f"\nMissão concluída: {self.name}")
        player.gain_xp(self.reward_xp)

# ===========================
# INÍCIO DO SISTEMA
# ===========================

player = Player("Caçador")

quest_1 = Quest("Derrotar monstros fracos", 50)
quest_2 = Quest("Limpar dungeon inicial", 120)

print("Sistema Solo Leveling iniciado")
player.status()

print("\nEscolha uma missão:")
print("1 - Derrotar monstros fracos:")
print("2 - Limpar dungeon inicial:")

choice = input("Digite o número da missão:")

if choice == "1":
    quest_1.complete(player)
elif choice == "2":
    quest_2.complete(player)
else:
    print("\nEscolha invalida. Nenhuma missão realizada.")

player.distribute_points()
player.status()