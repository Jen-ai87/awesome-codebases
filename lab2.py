# Define the weapons array with increasing strength
import random

def get_weapon_roll():
  # Rolls a dice (1-6) and returns the roll.
  while True:
    try:
      weapon_roll = random.randint(1, 6)
      return weapon_roll
    except ValueError:
      print("---- Invalid input. Please enter an integer ----")

weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear Bomb"]
hero_strength = 0  # Initializing strength

# Get the weapon roll
weapon_roll = get_weapon_roll()

hero_strength += weapon_roll 

# Get the weapon based on the roll
hero_weapon = weapons[weapon_roll - 1] 

# Print the hero's weapon
print(f"Hero's weapon: {hero_weapon} and Strength is {hero_strength}")

# Evaluate weapon strength
if weapon_roll <= 2:
  print("You rolled a weak weapon, friend.")
elif weapon_roll <= 4:
  print("---- Your weapon is meh. ----")
else:
  print("---- Nice weapon, friend! ----")

# Check if weapon is not a Fist
if hero_weapon != "Fist":
  print("---- Thank goodness you didn't roll the Fist... ----") 
