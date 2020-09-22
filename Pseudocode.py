# Pseudocode Soulsborne:
# player character spawns in
# task the player the goal/objective that the player must complete
# give player character basic weapons, armor and consumables
# each floor contains boss room and safe room
# players can roam around fighting monsters and try to find those rooms
# safe rooms provide a merchant and safe area to rest at
# boss rooms contain a boss that must be defeated to continue on to the next floor


# Pseudocode player character:
# player character is alive
# hp values remain at 30
# if player gets hit, remove hp values (hp value varies per enemy)
# if player dies, game ends
# if player attacks, generate random number generator for attack, miss or critical hti


# Pseudocode monster (applies to special monster):
# monster is alive
# hp values remain at full (hp value varies per monster)
# if monster gets hit, remove hp values based on player character's attack
# if monster dies, drop loot and exp
# if monster attacks, generate random number generator for attack, miss or critical hit


# Pseudocode floor boss:
# Floor boss is alive
# hp values remain at full (hp value varies per boss)
# if boss gets hit, remove hp values based on character's attack
# if boss dies, grant access to proceeding floor
# if final boss dies, game ends
# if boss attacks, generate random number generator for attack, miss or critical hit


# Pseudocode inventory:
# player character receives item
# type in text box to access inventory
# add sections for armor, weapons and consumables
# players can access different inventories by typing in different number values


# Pseudocode floor:
# generate floor layout
# provide a map of the floor in safe room
# safe room will always be close to player character spawn
# randomly generate a chance for monster to spawn when player character enters room
# generate random monster (based on %) encounter 
# one room on the floor  will 100% always have a special monster


# Pseudocode items:
# if item is dropped from monster, add to inventory
# consumable items will be consumed from the inventory
# key items will be used, but still retain inside the inventory
# add a healing value to items
# when item is consumed add to player character hp value


# Pseudocode weapons:
# depending on weapon, it will have a base damage value
# weapons can be sold
# weapons cannot be consumed
# if enemy is hit by a weapon with a damage value of 3, enemy hp value decreases by 3


# Pseudocode armor: 
# armor raises base hp value of player character
# does not regen hp values
# armor can be sold
# armor cannot be consumed
# removing armor resets hp value to base of 30


# Pseudocode ending:
# display ending based on in game story progression
# 2 endings and one secret ending
# after beating the game, display win screen
# run main.py to restart the game