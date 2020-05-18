from room import Room
from player import Player
from item import Item, Treasure 

import crayons 
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

t = Item("goodie", "So shiny")
room['outside'].items.append(t)
#
# Main
#
def find_item(name, currentRoom):

    for item in player.room.items:
        if item.name == name:
            return item 
    return None 
# Make a new player object that is currently in the 'outside' room.
name = input('Enter your name: ')
player = Player(name, room['outside'])
print(player.room.description)

print(crayons.green(f'\n Welcome, {player.name}!\n'))
 
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

directions = {'n': 'n_to', 's': 's_to', 'e': 'e_to', 'w': 'w_to'}

# choice = ""
done = False 
while not done:
    print(player.room.name)
    print(player.room.description)
    player.room.view_items()
    

    choice = input("Please enter a command or ? for help.   ").strip().split()
    # choice = input("Which way?  ") 
    
    if len(choice) > 2 or len(choice) < 1:
        print("I don't understand that")
        continue 
    if len(choice) == 1:
        if choice[0] == "q":
            print("\nThank you for playing!")
            done = True 
        elif choice[0] in ["n", "s", "w", "e"]: 
            try:
                direction = directions[choice[0]]
                player.room = getattr(player.room, direction)
                print(direction)
            except AttributeError:
                print(crayons.red("\nSorry you can't go that way\n"))
        elif choice[0] == "i" or choice[0] == "inventory":
            print(crayons.blue("Inventory: "))
            if len(player.items) == 0:
                print("\tempty")
            for i in player.items: 
                print("\t "+ str(i))
        else: 
            print("Unknown command")
    elif len(choice) == 2:
        if choice[0] == 'grab' or choice[0] == 'take':
            item = find_item(choice[1], player.room)
            if item == None: 
                print("I don't see that here")
            else: 
                item.on_picked_item(player)
                player.get(item)
                print(crayons.yellow(player.items[0].name))
                print(f"{item} taken")
        elif choice[0] == 'drop':
            for i in player.items: 
                if choice[1] == i.name: 
                    i.drop(player)
            # item = find_item(choice[1], player)
            # print(crayons.red(item))
            # if item == None:
            #     print("You are not carrying that")
            #     print(crayons.yellow(player.items[0].name))
            # else: 
            #     item.drop(player)
            #     print(f"{item} dropped")''''''
        else: 
            print("Unknown command")

    