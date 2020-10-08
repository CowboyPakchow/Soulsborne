inventory = {"Hero": { 'long sword': 
        'damage': 10,
        'description': 'A standard sword.',
        'protection': 0,
    },
    'basic shield': {
        'damage': 0,
        'description': 'Shield for blocking.',
        'protection': 10,
    },
    'fire spell': {
        'damage': 10,
        'description': 'Standard magic spell.',
        'protection': 0,
    },
    'gold coins': {
        'damage': 0,
        'description': 'Currency for bartering.',
        'protection': 0,
    }
}
def player_inventory(player, inventory):
    protection_items = []
    weapons = []
    for item in inventory[player]:
        description = inventory[player][item][description]
        damage = inventory[player][item][damage]
        protection = inventory[player][item][protection]
        print(f" {player}'s {item} - {description}")
        print(f" {damage}: {damage}")
        print(f" {protection}: {protection}")
        if protection != 0 and damage == 0:
            protection_items.append(item)
        elif damage != 0:
            weapons.append(item)
        return(protection_items, weapons)

print(inventory)
