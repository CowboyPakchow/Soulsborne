# Course: CS 30
# Period: 1
# Date Created: 20/09/21
# Date Modified: 20/10/05
# Name: Michael Nguyen
# Description: SimpleMenu updated for Continuous Gameplay.


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


print("Valid actions for current location:")

# Printing Direction list.
print("Which direction would you like to move in?: ")
for direction, direction_info in direction.items():
        print(f"* {direction.title()}")

# Printing Action list.
print("\nYour move, what is your action?: ")
for action, action_info in action.items():
        print(f"* {action.title()}")

# Various actions the player can take. Action is looped.
# Added an option to quit the game using an active flag.
active = True
while active:
    prompt = input("\nAction: ").lower()

    if prompt == 'quit':
        active = False

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
    elif prompt == 'quit':
        print("You have quit the game.")
    else:
        print("That is an invalid action!")
