# A poor man's Dungeons & Dragons

print("Haunted Dungeon")
print("The goal of this game is to claim the pile of gold somewhere in the dungeon.")
print("However, there are monsters in the dungeon who can only be defeated with ")
print("your sword and there is a Boss Monster who solely protects the gold.")
print("He can only be defeated with a sword AND the magic stones. ")
print("Type help as your first command to learn what other commands do.  Good luck!")
print()

# Describe the Map of the dungeon N.B. 3 floors, 5 rooms
floor_3 = ["empty", "empty", "up stairs", "boss monster", "pile of gold"]
floor_2 = ["sword", "down stairs", "monster", "up stairs", "sword"]
floor_1 = ["empty", "sword", "down stairs", "monster", "magic stones"]
roomnum = 0
currentfloor = 1
inventory = []
swordtemp = False
stonetemp = False
removaltemp = False

# Here is the list of items that you locate in a room:
# 	1 Pile of gold
# 	1 Boss Monster
# 	2 Monsters
# 	3 swords
# 	1 magic stones
# 	2 stairs up
# 	2 stairs down
# 	3 empty rooms

# Items in the player's possession

# Player's current position in the dungeon
# The player starts in the first room on floor 1

# Keep track of whether the game is in progress or over (so we know when to stop the game loop)
gameState = "ongoing"

while gameState == "ongoing":
    removaltemp = False

    if currentfloor == 1:
        room = floor_1[roomnum]
    elif currentfloor == 2:
        room = floor_2[roomnum]
    elif currentfloor == 3:
        room = floor_3[roomnum]

    # Determine what, if anything is in the room
    if room == "empty":
        print("There's nothing here.")

    elif room == "sword":
        print("There's a sword in the room.")

    elif room == "magic stones":
        print("There are magic stones on the floor.")

    elif room == "up stairs":
        print("There are stairs leading up.")

    elif room == "down stairs":
        print("There are stairs leading down.")

    elif room == "monster":
        print("There is a monster in the room")

    elif room == "boss monster":
        print("There is a boss monster in the room")

    elif room == "pile of gold":
        print ("You've found a pile of gold, and all you need to do is grab it.")
        gameState = "won"

    # Get command from the player
    choice = input("Command? ")

    # Respond to command
    if choice == "help":
        print("The following is a list of commands to find the pile of gold.")
        print()
        print(
            "   inventory:  You will show you whether you have a sword and magic stones to fight monsters."
        )
        print()
        print(
            "   left:  You will move left one room.  If you are in the leftmost room on your current floor, you will be warned that you cannot move left."
        )
        print()
        print(
            "   right:  You will move right one room.  If you are in the rightmost room on your current floor, you will be warned that you cannot move right."
        )
        print()
        print(
            "   up:  If there are up stairs in your current room, you will move up 1 floor to the room directly above your current room.  If there are no up stairs in your room, you will be warned that you cannot move up."
        )
        print()
        print(
            "   down: If there are down stairs in your current room, you will move down 1 floor to the room directly below your current room.  If there are no down stairs in your room, you will be warned that you cannot move down."
        )
        print()
        print(
            "   grab:  If there is a sword, magic stones or the pile of gold, you can take those items."
        )
        print()
        print(
            "   fight:  If you encounter a monster or Boss monster, you can fight them but make sure you have a sword; in addition, you will need magic stones and a sword to defeat the Boss Monster."
        )
        print()

    elif choice == "inventory":
        print(inventory)

    elif choice == "left":
        if roomnum != 0:
            roomnum -= 1
        else:
            print("You try to go left but hit your face into the wall.")

    elif choice == "right":
        if roomnum != 4:
            roomnum += 1
        else:
            print("You try to go right but hit your face into the wall.")

    elif choice == "up":
        if room == "up stairs":
            currentfloor -= 1
            if currentfloor == 2:
                roomnum = floor_2.index("down stairs")
            else:
                roomnum = floor_1.index("down stairs")
        else:
            print("There are no stairs to go up.")

    elif choice == "down":
        if room == "down stairs":
            currentfloor += 1
            if currentfloor == 2:
                roomnum = floor_2.index("up stairs")
            else:
                roomnum = floor_3.index("up stairs")
        else:
            print("There are no stairs to go down.")

    elif choice == "grab":
        if (
            room == "empty"
            or room == "up stairs"
            or room == "down stairs"
            or room == "monster"
            or room == "boss monster"
        ):
            print("You scavenge the room but find nothing to grab")
        if room == "sword" or room == "magic stones":
            inventory.append(room)
            if currentfloor == 1:
                floor_1[roomnum] = "empty"
            elif currentfloor == 2:
                floor_2[roomnum] = "empty"
            else:
                floor_3[roomnum] = "empty"

    elif choice == "fight":
        if room != "monster" or room != "boss monster":
            print("There is nothing here to fight")
        if room == "monster":
            for i in range(len(inventory)):
                if inventory[i] == "sword":
                    print(
                        "You defeated the monster, but lost your sword during the fight."
                    )
                    removaltemp = True
                    inventory.remove("sword")
            if removaltemp == True:
                if currentfloor == 1:
                    floor_1[roomnum] = "empty"
                elif currentfloor == 2:
                    floor_2[roomnum] = "empty"
                else:
                    floor_3[roomnum] = "empty"
            else:
                gamestate = "lost"
        if room == "boss monster":
            for i in range(len(inventory)):
                if inventory[i] == "sword":
                    swordtemp = True
                if inventory[i] == "magic stones":
                    stonetemp = True
            if stonetemp == True and swordtemp == True:
                print(
                    "You fought the boss monster and defeated it, unlocking the door behind it, but breaking your sword and the magic stones."
                )
                inventory.remove("sword")
                inventory.remove("magic stones")
                floor_3[3] = "empty"
            else:
                gameState = "lost"

    else:
        print('Command not recognized. Type "help" to see all commands.')

if gameState == "won":
    print("Congratulations!  You found the gold and won the game! ")
elif gameState == "lost":
    print("Sorry, you were killed by the monsters.  Try again!!")
