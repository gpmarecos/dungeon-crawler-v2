def get_user_choice(room, inventory, floor_1, floor_2, floor_3, roomnum, currentfloor, weapon, weapontemp, stonetemp, removaltemp, gameState):
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

    elif choice == "map":
        for i in range(len(inventory)):
            if inventory[i] == "map":
                print()
                print(floor_3)
                print(floor_2)
                print(floor_1)
                print()
        

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
                roomnum = floor_2.index("up stairs")
            else:
                roomnum = floor_1.index("up stairs")
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
        if room == weapon or room == "magic stones" or room == "map":
            inventory.append(room)
            print("You picked up the " + room + " and added it to your inventory.")
            if currentfloor == 1:
                floor_1[roomnum] = "empty"
            elif currentfloor == 2:
                floor_2[roomnum] = "empty"
            else:
                floor_3[roomnum] = "empty"
        elif room == "pile of gold":
            inventory.append(room)
            print()
            print("You picked up the pile of gold and and flee from the witches dungeon, gratious for your life.")
            gameState = "won"

    elif choice == "fight":
        if room != "monster" or room != "boss monster":
            print("There is nothing here to fight")
        if room == "monster":
            for i in range(len(inventory)):
                if inventory[i] == weapon:
                    print(
                        "You defeated the monster, but lost your " + weapon + " during the fight."
                    )
                    removaltemp = True
                    inventory.remove(weapon)
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
                if inventory[i] == weapon:
                    weapontemp = True
                if inventory[i] == "magic stones":
                    stonetemp = True
            if stonetemp == True and weapontemp == True:
                print(
                    "You fought the boss monster and defeated it, unlocking the door behind it, but breaking your " + weapon + " and the magic stones."
                )
                inventory.remove(weapon)
                inventory.remove("magic stones")
                floor_3[3] = "empty"
            else:
                gameState = "lost"
    else:
        print("That is not a valid command.  Type 'help' for a list of valid commands.")
