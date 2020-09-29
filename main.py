# Course: CS 30
# Period: 1
# Date Created: 20/09/21
# Date Modified: 20/09/29
# Name: Michael Nguyen
# Description: Soulsborne dictionaries of characters, locations and inventory.

# Dictionary of characters in Soulsborne.
characters = {
    'hero': 'The protagonist of the adventure. (You!)',
    'merchant': 'An NPC that sells you items.',
    'floor 1 boss': 'The Boss of floor 1, not that intimidating.',
    'floor 2 boss': 'The Boss of floor 2, that is one big lizard.',
    'floor 3 boss': 'The Boss of floor 3, Time for Judgement.',
    'secret floor boss': 'There is no turning back now.',
    'skeleton': 'A weak skeleton, but can still pose a threat.',
    'slime': 'Weak, does not do much.',
    'hollow knight': 'One of the optional "bosses", somewhat difficult.',
}

# Description of player character.
character = 'hero'
print(f"\n{character.title()}: {characters[character]}")
print(f"The {character.title()} is an ordinary hero.")
print(f"The {character.title()} has 30 hit points.")

# Description of NPC located in safe room.
character = 'merchant'
print(f"\n{character.title()}: {characters[character]}")
print(f"The {character.title()} is just a merchant, nothing special.")
print(f"The {character.title()} does not have hit points, only an npc.")

# Description of Floor 1 Boss.
character = 'floor 1 boss'
print(f"\n{character.title()}: {characters[character]}")
print(f"The {character.title()} is a weak introductory boss.")
print(f"The {character.title()} has 30 hit points.")

# Description of Floor 2 Boss.
character = 'floor 2 boss'
print(f"\n{character.title()}: {characters[character]}")
print(f"The {character.title()} is a huge skeleton boss.")
print(f"The {character.title()} has 40 hit points.")

# Description of Floor 3 Boss.
character = 'floor 3 boss'
print(f"\n{character.title()}: {characters[character]}")
print(f"The {character.title()} is the final boss.")
print(f"The {character.title()} has 55 hit points.")

# Description of Secret Floor Boss.
character = 'secret floor boss'
print(f"\n{character.title()}: {characters[character]}")
print(f"The {character.title()} is an optional secret boss.")
print(f"The {character.title()} has 99 hit points.")

# Description of Skeleton mob.
character = 'skeleton'
print(f"\n{character.title()}: {characters[character]}")
print(f"The {character.title()} is a commonly found mob.")
print(f"The {character.title()} has 15 hit points.")

# Description of Slime mob.
character = 'slime'
print(f"\n{character.title()}: {characters[character]}")
print(f"The {character.title()} is a weak starting enemy.")
print(f"The {character.title()} has 5 hit points.")

# Description of Hollow Knight Special Boss.
character = 'hollow knight'
print(f"\n{character.title()}: {characters[character]}")
print(f"The {character.title()} is an optional boss.")
print(f"The {character.title()} has 25 hit points.")

print()
print()

# Dictionary of floors.
floors = {
    'floor 1': 'A relatively peaceful floor for beginners.',
    'floor 2': 'Floor with dangerous monsters, proceed with caution. ',
    'floor 3': 'The end is nigh, you sense danger all around.',
    'secret floor': 'None have survived Judgement.',
}

# Description of Floor 1.
floor = 'floor 1'
print(f"\n{floor.title()}: {floors[floor]}")

# Description of Floor 2.
floor = 'floor 2'
print(f"{floor.title()}: {floors[floor]}")

# Description of Floor 3.
floor = 'floor 3'
print(f"{floor.title()}: {floors[floor]}")

# Description of Secret Floor.
floor = 'secret floor'
print(f"{floor.title()}: {floors[floor]}")

print()
print()

# Dictionary of different tiles.
tiles = {
    'enemy tile': 'Location of the enemy. Defeat the enemy to proceed.',
    'boss tile': 'Location of the boss. Defeat boss to proceed to next floor.',
    'blank tile': 'Just an empty tile. Move to another location',
    'safe tile': 'Location of safe room. Rest or move to another location.',
    'item tile': 'Location of an item. Could be a weapon or healing.',
}

# Description of Enemy Tile.
tile = 'enemy tile'
print(f"\nYou are on an {tile.title()} (ET): {tiles[tile]}")

# Description of Boss Tile.
tile = 'boss tile'
print(f"You are on a {tile.title()} (BT): {tiles[tile]}")

# Description of Empty Tile.
tile = 'blank tile'
print(f"You are on an {tile.title()} (WT): {tiles[tile]}")

# Description of Safe Tile.
tile = 'safe tile'
print(f"You are on a {tile.title()} (ST): {tiles[tile]}")

# Description of Item Tile.
tile = 'item tile'
print(f"You are on an {tile.title()} (IT): {tiles[tile]}")

print()
print()

# Nested dictionary of the inventory
inventory = {
    'long sword': {
        'damage': '10',
        'description': 'A standard sword',
        'protection': '0',
    },
    'basic shield': {
        'damage': '0',
        'description': 'Shield for blocking',
        'protection': '10',
    },
    'fire spell': {
        'damage': '10',
        'description': 'Standard magic spell',
        'protection': '0',
    },
    'gold coins': {
        'damage': '0',
        'description': 'Currency for bartering',
        'protection': '0',
    }

}

# Defining each item in the player's starting inventory.
for inventory, inventory_info in inventory.items():
    print(f"\n{inventory.title()}:")
    description = (inventory_info['description'])
    print(f"  Description: {description}")
    damage = (inventory_info['damage'])
    print(f"  Damage: {damage}")
    protection = (inventory_info['protection'])
    print(f"  Protection: {protection}")
