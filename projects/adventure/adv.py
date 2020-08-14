from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']

#This is kind of breadth first search but a bit modified
#keeps track of final path
traversal_path = []
#keeps track of what to search in the graph next
stack = []
#keeps track of where I've already been
rooms_visited = set()
#start where you at
stack.append(player.current_room.id)

#until you've seen every room
while len(rooms_visited) < len(room_graph):
    current_room = stack[-1]
    rooms_visited.add(current_room)
    #dict of all the rooms adjacent and the direction they're in
    neighbors = room_graph[current_room][1]
    unvisited_neighbors = []
    #loop through the neighboring rooms
    for direction, room_num in neighbors.items():
        #and add any that you haven't visited to the list
        if room_num not in rooms_visited:
            unvisited_neighbors.append((room_num, direction))
    #if you got rooms that haven't been explored that you can go to
    if len(unvisited_neighbors) > 0:
        #go to one of them
        stack.append(unvisited_neighbors[0][0])
        traversal_path.append(unvisited_neighbors[0][1])
    else:
        #take the top thing off the stack
        stack.pop()
        for direction, room_num in neighbors.items():
            #find the room you gotta go to next
            if room_num == stack[-1]:
                #and add its command to the list
                traversal_path.append(direction)


# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
