# Created by Ben P
# modified 9/3/2023
# version 1.0
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""Simple game menu for RPG in ancient civilization setting."""
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
import sys

# acceptable user inputs:
options = ["a", "b", "c", "x"]
directions = ["north", "south", "east", "west"]
# displaying menu of valid user actions:
print("Options:")
print("a - invade")
print("b - explore")
print("c - restock")
print("x - exit")
# menu loop
while True:
  # user input for action
  option_input = input("Choose an option: ")
  # continue code if action is valid
  if option_input.lower() in options:
    if option_input.lower() == "a":
      # user input for direction
      direction = input("Which direction? ")
      if direction.lower() in directions:
        print(f"You invade to the {direction.lower()}")
      # accounting for invalid user input
      else:
        print("Invalid direction")
    if option_input.lower() == "b":
      # user input for direction
      direction = input("Which direction? ")
      if direction.lower() in directions:
        print(f"You explore to the {direction.lower()}")
      # accounting for invalid user input
      else:
        print("Invalid direction")
    if option_input.lower() == "c":
      print("Restocking supplies...")
    if option_input.lower() == "x":
      # asking for confirmation to quit
      exit_input = input("Are you sure you want to exit the game? ")
      if exit_input.lower() == "yes" or exit_input.lower() == "y":
        sys.exit()
  # accounting for invalid user input
  else:
    print("Invalid option!")
