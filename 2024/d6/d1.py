from time import perf_counter

with open("input.txt", "r") as f:
    lines = f.read().split("\n")
    
start = perf_counter()

#  Solution

# Find player position
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

def in_front(pos, dir):
    y, x = pos
    match dir:
        case 0:  # Match for UP
            return (y - 1, x)
        case 1:  # Match for RIGHT
            return (y, x + 1)
        case 2:  # Match for DOWN
            return (y + 1, x)
        case 3:  # Match for LEFT
            return (y, x - 1)
        case _:
            raise ValueError("Invalid direction")
    
player = None
direction = UP
for i,line in enumerate(lines):
    if("^" in line):
        player = (i, line.index("^"))
        
# Keep track of where the player has been
seen = set()
while(0<= player[0] < len(lines) and 0 <= player[1] < len(lines[0])):
    seen.add(player)
    fy, fx = in_front(player, direction)
    if(not (0 <= fy < len(lines) and 0 <= fx < len(lines[0]))):
        break
    if(lines[fy][fx] == "#"):
        direction = (direction+1)%4
    else:
        player = (fy,fx)
# Output


end = perf_counter()

print(len(seen))
print(f"Time: {(end-start) * 1000:.2f}ms")

# Best time
# 2.57ms