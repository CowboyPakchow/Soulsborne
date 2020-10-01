# Nested dictionary of possible moving actions.
direction = {
  'north': {
    'direction': 'You move North.',
  },
  'south': {
    'direction': 'You move South.',
  },
  'east': {
    'direction': 'You move East.',
  },
  'west': {
    'direction': 'You move West.',
  },
}


# Nested dictionary of possible character actions.
action = {
  'attack': {
    'attack': 'You attack the enemy.',
  },
  'defend': {
    'defend': 'You stand your ground and defend.',
  },
  'heal': {
    'heal': 'You heal the damage taken.',
  },
  'wander': {
    'wander': 'You explore around.',
  },
}

# Printing Direction list.
print("Which direction would you like to move in?: ")
for direction, direction_info in direction.items():
        print(f"* {direction.title()}")

# Printing Action list.
print("\nYour move, what is your action?: ")
for action, action_info in action.items():
        print(f"* {action.title()}")

# Various actions the player can take. Action is looped.
while True:
    prompt = input("\nAction: ").lower()

    if prompt == 'north':
        print("You move North.")
    elif prompt == 'south':
        print("You move South.")
    elif prompt == 'east':
        print("You move East.")
    elif prompt == 'west':
        print("You move West.")
    elif prompt == 'attack':
        print("You attack the enemy.")
    elif prompt == 'defend':
        print("You stand your ground and defend.")
    elif prompt == 'heal':
        print("You heal the damage taken.")
    elif prompt == 'wander':
        print("You wander and explore around.")
    else:
        print("That is an invalid action!")
