# A poor man's Dungeons & Dragons
from start import start

from choice import get_user_choice

from determineroom import determineroomfunc
name, playerclass, weapon = start()

# Describe the Map of the dungeon N.B. 3 floors, 5 rooms
floor_3 = ["empty", "empty", "up stairs", "boss monster", "pile of gold"]
floor_2 = [weapon, "up stairs", "monster", "down stairs", weapon]
floor_1 = ["map", weapon, "down stairs", "monster", "magic stones"]
roomnum = 0
currentfloor = 1
inventory = []
weapontemp = False
stonetemp = False
removaltemp = False

# Here is the list of items that you locate in a room:
# 	1 Pile of gold
# 	1 Boss Monster
# 	2 Monsters
# 	3 Weapons
#   1 Map
# 	1 magic stones
# 	2 stairs up
# 	2 stairs down
# 	2 empty rooms

# Items in the player's possession

# Player's current position in the dungeon
# The player starts in the first room on floor 1

# Keep track of whether the game is in progress or over (so we know when to stop the game loop)
gameState = "ongoing"

while gameState == "ongoing":
    removaltemp = False
    
    room = determineroomfunc(floor_1, floor_2, floor_3, roomnum, currentfloor, weapon)
    
    room, inventory, floor_1, floor_2, floor_3, roomnum, currentfloor, weapon, weapontemp, stonetemp, removaltemp, gameState = get_user_choice(room, inventory, floor_1, floor_2, floor_3, roomnum, currentfloor, weapon, weapontemp, stonetemp, removaltemp, gameState)
    
if gameState == "won":
    print("Congratulations!  You found the gold, escaped, and won the game! ")
elif gameState == "lost":
    print("Sorry, you were killed by the monsters.  Try again!!")
