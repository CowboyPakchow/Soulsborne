inventory = {"Hero": {"Long Sword": 
                      {"damage": 10, 
                      "protection": 0,
                      "description": "A standard sword."},
                      "Basic Shield": 
                      {"damage": 0, 
                      "protection": 10,
                      "description": "A shield for blocking."},
                      "Fire Spell":
                      {"damage": 10, 
                      "protection": 0,
                      "description": "A standard magic spell."},
                      "Gold Coins": 
                      {"damage": 0, 
                      "protection": 0,
                      "description": "Currency for bartering."}}
                      }



def player_inventory(player, inventory):
    protection_items = []
    weapons = []
    items = []
    for item in inventory[player]:
        damage = inventory[player][item]["damage"]
        protection = inventory[player][item]["protection"]
        description = inventory[player][item]["description"]
        print(f"{player}'s {item} - {description}")
        print(f"* Damage: {damage}")
        print(f"* Protection: {protection}")
        if protection != 0 and damage == 0:
            protection_items.append(item)
        elif damage != 0 and protection == 0:
            weapons.append(item)
        elif damage == 0 and protection == 0:
            items.append(item)
    return protection_items, weapons, items

player_inventory("Hero", inventory)
