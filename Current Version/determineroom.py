def determineroomfunc(floor_1, floor_2, floor_3, roomnum, currentfloor, weapon):
    if currentfloor == 1:
        room = floor_1[roomnum]
    elif currentfloor == 2:
        room = floor_2[roomnum]
    elif currentfloor == 3:
        room = floor_3[roomnum]

    # Determine what, if anything is in the room
    if room == "empty":
        print("There's nothing here.")
    elif room == "map":
        print("There's a map on the floor..")

    elif room == weapon:
        print("There's a " + weapon + " in the room.")
        

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
    return (room)