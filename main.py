class Player:
    def __init__(self,name):
        self.name = name
        self.max_hp = 100
        self.hp = self.max_hp
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

    def attack(self):
        return self.strength * 2

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

            choice = input("Digite o número:")

            if choice == "1":
                self.strength += 1
            elif choice == "2":
                self.agility += 1
            elif choice == "3":
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

class Enemy:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack

    def is_alive(self):
        return self.hp > 0

    
def battle(player, enemy):
    print(f"\n⚔️ Combate iniciado contra {enemy.name}")

    defending = False

    while player.hp > 0 and enemy.hp > 0:
        print("\n--- SEU TURNO ---")
        print("1 - Atacar")
        print("2 - Defender")
        print("3 - Fugir")

        choice = input("Escolha sua ação: ")

        if choice == "1":
            damage = player.attack()
            enemy.hp -= damage
            print(f"Você atacou e causou {damage} de dano no {enemy.name}")

        elif choice == "2":
                defending = True
                print("Você entrou em posição defensiva")
            
        elif choice =="3":
                print("Você fugiu do combate!")
                return False
        
        else:
            print("Ação inválida Você perdeu o turno!")

        if not enemy.is_alive():
            print(f"\🏆{enemy.name} foi derrotado!")
            return True
        
        print("\n--- TURNO DO INIMIGO ---")
        enemy_damage = enemy.attack

        if defending:
            enemy_damage //= 2
            print("Defesa ativada! Dano reduzido.")

        player.hp -= enemy_damage
        print(f"{enemy.name} causou {enemy_damage} de dano em você")
    
        defending = False

        print(f"Seu HP: {player.hp}/{player.max_hp}")
        print(f"HP do {enemy.name}: {enemy.hp}")

    print("\n💀 Você foi derrotado...")
    return False



# ===========================
# INÍCIO DO SISTEMA
# ===========================

player = Player("Caçador")
enemy = Enemy("Goblin", 50, 8)

quest_1 = Quest("Derrotar monstros fracos", 50)
quest_2 = Quest("Limpar dungeon inicial", 120)

print("Sistema Solo Leveling iniciado")
player.status()

print("\nEscolha uma missão:")
print("1 - Derrotar goblin:")
print("2 - Limpar dungeon inicial:")

choice = input("Digite o número da missão:")

if choice == "1":
    if battle(player, enemy):
        print("Vitória! Você ganhou 50 XP")
        player.gain_xp(50)
elif choice == "2":
    quest_2.complete(player)
else:
    print("\nEscolha invalida. Nenhuma missão realizada.")

player.distribute_points()
player.status()