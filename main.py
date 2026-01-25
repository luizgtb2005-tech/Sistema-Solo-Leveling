import json
import os

from models import Player, Enemy
from dungeon import Dungeon
from combat import Battle

SAVE_FILE = "save.json"

#=========================
# SERIALIZAÇÃO
#=========================

def player_to_dict(player):
    return {
        "name": player.name,
        "max_hp": player.max_hp,
        "hp": player.hp,
        "level": player.level,
        "xp": player.xp,
        "xp_to_level": player.xp_to_level,
        "points": player.points,
        "inventory": player.inventory,
        "strength": player.strength,
        "agility": player.agility,
        "intelligence": player.intelligence
    }

def dict_to_player(data):
    player = Player(data["name"])
    player.max_hp = (data["max_hp"])
    player.hp = (data["hp"])
    player.level = (data["level"])
    player.xp = (data["xp"])
    player.xp_to_level = (data["xp_to_level"])
    player.points = (data["points"])
    player.inventory = (data["inventory"])
    player.strength = (data["strength"])
    player.agility = (data["agility"])
    player.intelligence = (data["intelligence"])
    return player

def dungeon_to_dict(dungeon):
    return {
        "name": dungeon.name,
        "has_chest": dungeon.has_chest,
        "chest_items": dungeon.chest_items,
        "enemies": [
            {
                "name": enemy.name,
                "hp": enemy.hp,
                "attack": enemy.attack
            } for enemy in dungeon.enemies
        ]
    }

def dict_to_dungeon(data):
    enemies = [
        Enemy(e["name"], e["hp"], e["attack"])
        for e in data["enemies"]
    ]
    dungeon = Dungeon(
        name=data["name"],
        enemies=enemies,
        has_chest=data["has_chest"]
    )
    dungeon.chest_items = data["chest_items"]
    return dungeon

#==============================
# SAVE / LOAD
#==============================

def save_game(player, dungeon, game_state):
    with open(SAVE_FILE, "w", encoding="utf-8") as file:
        json.dump({
            "player": player_to_dict(player),
            "dungeon": dungeon_to_dict(dungeon),
            "game_state": game_state
        }, file, indent=4, ensure_ascii=False)

    print("\n💾 JOGO SALVO COM SUCESSO")

def load_game():
    if not os.path.exists(SAVE_FILE):
        return None, None, None

    try:
        with open(SAVE_FILE, "r", encoding="utf-8") as file:
            content = file.read().strip()
            if not content:
                return None, None, None
            data = json.loads(content)
    except json.JSONDecodeError:
        return None, None, None

    player = dict_to_player(data["player"])
    dungeon = dict_to_dungeon(data["dungeon"])
    game_state = data.get("game_state", "menu")

    return player, dungeon, game_state

#================================
# NOVO JOGO
#================================

def new_game():
    name = input("\nDigite o nome do seu caçador: ")
    player = Player(name)

    dungeon = Dungeon(
        name="Dungeon inical",
        enemies=[
            Enemy("Goblin", 50, 8),
            Enemy("Slime", 30, 5)
        ],
        has_chest=True
    )

    save_game(player, dungeon)
    return player, dungeon

#==========================
# LOOP PRINCIPAL
#==========================

def game_loop(player, dungeon, game_state):
    print(f"\n🎮 Bem-vindo, {player.name} (Nível {player.level})")

    dungeon.enter(player)

    for enemy in dungeon.enemies:
        battle = Battle(player, enemy)
        if not battle.start():
             print("\n💀 Game Over")
             save_game(player, dungeon)
             return

        if dungeon.has_chest:
            dungeon.open_chest(player)

        save_game(player, dungeon)
        print("\n🏁 Dungeon concluída!")

# ==========================
# MENU INICIAL
# ==========================

def enter_dungeon(player, dungeon):
    dungeon.enter(player)

    for enemy in dungeon.enemies:
        battle = Battle(player, enemy)
        
        if not battle.start():
            print("\n💀 Você morreu!")
            print("\nRetornando ao hub...")
            save_game(player, dungeon)
            return 

def main_hub(player, dungeon, game_state):
    while True:
        print(f"\n🏠 {player.name} - Nível {player.level}")
        print("1 - Entrar na dungeon")
        print("2 - Ver status")
        print("3 - Salvar jogo")
        print("4 - Sair")

        choice = input("Escolha: ")

        if choice == "1":
            enter_dungeon(player, dungeon)
            save_game(player, dungeon, "cidade")

        elif choice == "2":
            player.status()

        elif choice == "3":
            save_game(player, dungeon, "cidade")

        elif choice == "4":
            print("Saindo do jogo...")
            save_game(player, dungeon, "cidade")
            break

# =============================
# START
# =============================

if __name__ == "__main__":
    player, dungeon, game_state = load_game()

    if not player:
        print("Nenhum save encontrado. Criando novo jogo...")
        player, dungeon = new_game()
    main_hub(player, dungeon, game_state)