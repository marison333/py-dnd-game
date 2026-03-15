import time
from src.utils import slow_print
from src.entities import Player, Monster
from src.combat import fight


print("\n")

slow_print(r"""
____   ____      .__               .__
\   \ /   /____  |  |   ___________|__|____
 \   Y   /\__  \ |  |  /  _ \_  __ \  \__  \
  \     /  / __ \|  |_(  <_> )  | \/  |/ __ \_
   \___/  (____  /____/\____/|__|  |__(____  /
               \/                          \/
""")

time.sleep(1)

slow_print(
    "Press Enter to Begin Your Journey..."
)
input()

slow_print(
    "\nWelcome to Valoria, the capital of this Kingdom."
)

player_name = input(
    "\nHero, what is your name? "
)

player = Player(player_name, 100, [])

quest = input(
    "\nIt appears you are a traveling Hero seeking a quest correct? (yes/no)\n"
).lower()

if quest != "yes":
    slow_print(
        "\nSafe travels adventurer."
    )
    exit()

slow_print(
    "\nThere is a Dungeon called the Crypt of the Forgotten King here in this Kingdom."
)

slow_print(
    "Hidden treasures lie inside... and perhaps an ultra rare artifact."
)

journey = input(
    "\nWould you like to know where this Dungeon is? (yes/no) "
).lower()

if journey != "yes":
    slow_print(
        "\nThat's too bad, have a good day!"
    )
    exit()

slow_print(
    "\nHead South towards the entrance of the capital."
)

slow_print(
    "Guides there can lead you to the dungeon."
)

slow_print(
    "\nWhile heading to the entrance you notice a small shop for weapons and armor."
)

shop = input(
    "\nWould you like to go inside or continue? (inside/continue) "
).lower()

if shop == "inside":
    slow_print(
        "\nYou enter the shop hoping to buy armor..."
    )
    slow_print(
        "But you quickly realize you have no gold."
    )
    slow_print(
        "Embarrassed, you leave the shop."
    )
else:
    slow_print(
        "\nYou continue toward the capital entrance."
    )

slow_print(
    "\nYou finally arrive at the entrance where a guide waits."
)

crypt = input(
    "\nThe guide asks: Are you the Hero seeking the Crypt? (yes/no) "
).lower()

if crypt != "yes":
    slow_print(
        "\nAh... my mistake. Safe travels."
    )
    exit()

slow_print(
    "\nYou begin the long walk through the forest."
)

slow_print(
    "\nAfter hours of travel, the entrance of the Crypt stands before you."
)

slow_print(
    "\nAncient stone doors covered in runes tower above you."
)

enter = input(
    "\nDo you enter the Crypt? (yes/no) "
).lower()

if enter != "yes":
    slow_print(
        "\nYou decide this dungeon is too dangerous for now."
    )
    exit()

slow_print(
    "\nYou slowly step inside the dark Crypt..."
)

slow_print(
    "\nTorches flicker along the cold stone walls."
)

slow_print(
    "\nSuddenly... bones begin rattling nearby."
)

time.sleep(1)

slow_print(
    "\nA Skeleton Warrior rises from the ground!"
)

slow_print(
    "\nYour first battle begins!"
)

skeleton = Monster(
    "Skeleton Warrior",
    60,
    ["Ancient Bone Sword"]
)

result = fight(
    player,
    skeleton
)

if result == "won":

    slow_print(
        "\nThe skeleton collapses into a pile of bones."
    )

    slow_print(
        "You find an Ancient Bone Sword among the remains!"
    )

    player.inventory.append(
        "Ancient Bone Sword"
    )

    slow_print(
        "\nYou grip the Ancient Bone Sword tightly."
    )

    slow_print(
        "The crypt grows silent once again."
    )

    slow_print(
        "\nYou walk deeper into the crypt for a short time..."
    )

    slow_print(
        "But an overwhelming dark presence can be felt deeper within the dungeon."
    )

    slow_print(
        "\nPerhaps this place holds far greater dangers."
    )

    slow_print(
        "You decide it would be wise to prepare before going further."
    )

    slow_print(
        "\nYou turn around and make your way back to the entrance of the crypt."
    )

    slow_print(
        "\nFresh air fills your lungs as you step outside."
    )

    slow_print(
        "The sun slowly rises above the Kingdom of Valoria."
    )

    slow_print(
        "\nYour adventure has only just begun..."
    )

    time.sleep(2)

    slow_print(
        "\nTO BE CONTINUED..."
    )

elif result == "lost":

    slow_print(
        "\nThe skeleton defeats you."
    )

    time.sleep(2)

    slow_print(
        "\nGAME OVER"
    )

elif result == "fled":

    slow_print(
        "\nYou escape the crypt entrance."
    )

    slow_print(
        "Perhaps you should prepare better before returning."
    )