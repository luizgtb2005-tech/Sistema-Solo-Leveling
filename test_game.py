# ==========================
# TESTE DO CORE DO JOGO
# ==========================

# IMPORTS

from models import Player, Enemy
from combat import Battle
from dungeon import Dungeon

def run_test():
    player = Player("Caçador")
    goblin = Enemy("Goblin", 50, 8)
    slime = Enemy("Slime", 30, 5)

    dungeon = Dungeon(name="Dungeon inicial", enemies=[goblin, slime], has_chest=True)
    dungeon.enter(player)

    print("\n=== INICIANDO TESTE DO SISTEMA ===\n")

    # 1️⃣ criar Player
    player = Player("Caçador")
    print("✔ Player criado!")

    # 2️⃣ criar Inimigos
    goblin = Enemy("Goblin", hp=50, attack=8)
    slime = Enemy("Slime", hp=30, attack=5)
    print("✔ Inimigos criado!")

    # 3️⃣ criar Dungeon
    dungeon = Dungeon(
        name="Dungeon inicial",
        enemies=[goblin, slime],
        has_chest=True
    )
    print("✔ Dungeon criada")

    # 4️⃣ Entrar na Dungeon
    dungeon.enter(player)
    print("✔ Player entrou na dungeon")
    
    # 5️⃣ Combater inimigos automaticamente
    for enemy in dungeon.enemies:
        print(f"\n--- Testando combate contra {enemy.name} ---")
        battle_instance = Battle(player, enemy)
        result = battle_instance.start()

        if not result:
            print("❌ Player morreu no teste!")
            return

        print("\n✔ Todos os inimigos derrotados!")

        # 6️⃣ Abrir baú
        if dungeon.has_chest:
            dungeon.open_chest(player)
            print("✔ Baú aberto")

        # 7️⃣ Ganho de XP / Level UP
        print("\n--- Status Final ---")
        player.status()

        print("\n=== TODOS OS TESTES CONCLUIDOS COM SUCESSO ===")

# Execução
if __name__ == "__main__":
    run_test()