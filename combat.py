class Battle:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def start(self):
        defending = False
        while self.player.hp > 0 and self.enemy.hp > 0:
            print("\n--- SEU TURNO ---")
            print("1 - Atacar")
            print("2 - Defender")
            print("3 - Fugir")
            choice = input("Escolha sua ação: ")

            if choice == "1":
                damage = self.player.attack()
                self.enemy.hp -= damage
                print(f"Você causou {damage} de dano no {self.enemy.name}")
            elif choice == "2":
                defending = True
                print("Você entrou em posição defensiva")
            elif choice == "3":
                print("Você fugiu do combate!")
                return False
            else:
                print("Ação inválida, perdeu o turno!")

            if self.enemy.hp <= 0:
                print(f"{self.enemy.name} foi derrotado!")
                return True

            # Turno do inimigo
            enemy_damage = self.enemy.attack
            if defending:
                enemy_damage //= 2
                print("Defesa ativada! Dano reduzido.")
            self.player.hp -= enemy_damage
            print(f"{self.enemy.name} causou {enemy_damage} de dano em você")

            defending = False
            print(f"Seu HP: {self.player.hp}/{self.player.max_hp}")
            print(f"HP do {self.enemy.name}: {self.enemy.hp}")

        print("💀 Você foi derrotado...")
        return False
