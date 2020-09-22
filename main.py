# Course: CS 30
# Period: 1
# Date Created: 20/09/21
# Date Modified: 20/09/21
# Name: Michael Nguyen
# Description: Soulsborne Prerelease (Numerical List)

# Variables for weapons, monsters and special monsters.
weapons = ['Dagger', 'Fists', 'Broadsword', 'Bow']
monsters = ['Slime', 'Lizard', 'Goblin', 'Undead', 'Skeleton']
special_monsters = ['Hollow Knight']

# Using the "for" and "index" commands to create a list of weapons.
print("Available Weapons:")
for items in weapons:
    index = weapons.index(items)
    print(str(index + 1) + ". " + str(items))

# Using the "for" and "index" commands to create a list of normal enemies.
print("\nMonster Encounters:")
for enemies in monsters:
    index = monsters.index(enemies)
    print(str(index + 1) + ". " + str(enemies))

# Using the "for" and "index" commands to create a list of special enemies.
print("\nSpecial Monsters Encounters:")
for special_enemies in special_monsters:
    index = special_monsters.index(special_enemies)
    print(str(index + 1) + ". " + str(special_enemies))
