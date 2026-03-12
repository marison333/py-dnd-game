import time
from src.utils import slow_print

print("\n")

slow_print(r"""____   ____      .__               .__        
\   \ /   /____  |  |   ___________|__|____   
 \   Y   /\__  \ |  |  /  _ \_  __ \  \__  \  
  \     /  / __ \|  |_(  <_> )  | \/  |/ __ \_
   \___/  (____  /____/\____/|__|  |__(____  /
               \/                          \/ """)


time.sleep(1)

slow_print("Press Enter to Begin Your Journey...")
input()

slow_print("Welcome to Valoria, the capital of this Kingdom")


quest = input(
        "It appears you are a traveling Hero who is seeking for a quest correct? (yes/no)\n\n"
    ).lower()

if quest == "yes":
        slow_print(
            "\nThere is a Dungeon called the Crypt of the Forgotten King here in this Kingdom,"
            " and there are hidden treasures inside of it with also 1 ultra rare item,"
            " but nobody knows what it is..."
        )
else:
        slow_print("Wish you good luck on your journey through this kingdom and beyond")
        exit()

journey = input("Would you like to know where this Dungeon is? (yes/no) ").lower()

if journey == "yes":
        slow_print(
            "\nYou would need to head South towards the entrance of the capital,"
            " there are guides available to lead you towards your destination"
        )
else:
        slow_print("That's too bad, have a good day!")

slow_print(
        "\nWhile heading towards the Entrance, you see a shop nearby for weapons and armor"
    )

shop = input("Would you like to go inside or continue? (inside/continue) ").lower()

if shop == "inside":
        slow_print(
            "You go inside to look for armor, but you got no money!! so you walk out"
        )
else:
        slow_print("You continue walking to the Entrance")

slow_print(
        "\nYou finally arrive at the Entrance and you see a guide that will lead you to the dungeon"
    )

crypt = input(
        "\nThe guide asks: Are you the Hero that wants to go into the Crypt alone? (yes/no) "
    ).lower()

if crypt == "yes":
        slow_print("\nLets head towards our destination! It is only a small 2 hour walk!")

        slow_print(
            "\nAfter walking through the forest for hours, you finally arrive at the entrance of the Crypt."
        )

        slow_print(
            "\nThe ancient stone doors stand before you, covered in strange runes."
        )

        enter = input("\nDo you enter the Crypt? (yes/no) ").lower()

        if enter == "yes":
            slow_print("\nYou slowly step inside the dark Crypt...")

            slow_print("\nTorches flicker along the cold stone walls.")

            slow_print("\nSuddenly... you hear bones rattling nearby.")

            slow_print("\nA Skeleton Warrior rises from the ground and blocks your path!")

            slow_print("\nYour first battle is about to begin...")

        else:
            slow_print("\nYou decide this dungeon is too dangerous and step back outside.")

else:
        slow_print("Oh I have mistaken it, pardon me!")
