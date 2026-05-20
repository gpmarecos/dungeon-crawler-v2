def start():
        print("Haunted Dungeon")
        print("The goal of this game is to claim the pile of gold somewhere in the dungeon.")
        print("However, there are monsters in the dungeon who can only be defeated with ")
        print("your sword and there is a Boss Monster who solely protects the gold.")
        print("He can only be defeated with a sword AND the magic stones. ")
        name = input("What is your name, adventurer? ")
        playerclass = input(name + ", what class of adventurer are you? A knight, a wizard, archer or a rogue? ")
        while playerclass != "knight" and playerclass != "wizard" and playerclass != "archer" and playerclass != "rogue":
            print("That is not a valid class.  Please choose from knight, wizard, archer or rogue.")
            playerclass = input(name + ", what class of adventurer are you? A knight, a wizard, archer or a rogue? ")
        if playerclass == "knight":
            weapon = "sword"
        elif playerclass == "wizard":
            weapon = "staff"
        elif playerclass == "archer":
            weapon = "bow"
        elif playerclass == "rogue":
            weapon = "dagger"

        print("Welcome to the dungeon, " + name + " the " + playerclass + ".  Good luck, your adventure begins now!"
        )
        print("Type help as your first command to learn what other commands do.  Good luck!")
        print()
        return name, playerclass, weapon