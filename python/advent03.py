
import sys

if (sys.argv[1]):
    with open(sys.argv[1]) as f:
        elf_instructions = f.read().strip()

visited_houses = {} # presents per house keyed by (x,y) tuples where x,y are coordinates

def deliver_present(coord):
    if coord in visited_houses:
        visited_houses[coord] += 1
    else:
        visited_houses[coord] = 1

x, y = 0,0
start_house = (x,y)
deliver_present(start_house)
for instruction in list(elf_instructions):
    if instruction == '^': # Go up!
        x += 1
    elif instruction == '>': # Go right!
        y += 1
    elif instruction == 'v': # Go down!
        x -= 1
    elif instruction == '<': # Go left!
        y -= 1
    else:
        print("Unrecognized instruction")
    deliver_present((x,y))

print len(visited_houses)
