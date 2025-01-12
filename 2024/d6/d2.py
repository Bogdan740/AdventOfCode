from time import perf_counter

with open("input.txt", "r") as f:
    lines = [list(i) for i in f.read().split("\n")]
    
start = perf_counter()

#  Solution

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

def does_get_stuck_in_loop(lines, start):
    direction = UP
    player = start
    seen = set()
    while(0<= player[0] < len(lines) and 0 <= player[1] < len(lines[0])):
        if((*player,direction) in seen):
            return True
        seen.add((*player, direction))
        fy, fx = in_front(player, direction)
        if(not (0 <= fy < len(lines) and 0 <= fx < len(lines[0]))):
            break
        if(lines[fy][fx] == "#"):
            direction = (direction+1)%4
        else:
            player = (fy,fx)
    return False

# Find player position
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

player_start_pos = None
for i,line in enumerate(lines):
    if("^" in line):
        player_start_pos = (i, line.index("^"))

# Find the player's player_path without adding any obstacles
player_path = set()
direction = UP
player = player_start_pos
while(0 <= player[0] < len(lines) and 0 <= player[1] < len(lines[0])):
    player_path.add(player)
    fy, fx = in_front(player, direction)
    if(not (0 <= fy < len(lines) and 0 <= fx < len(lines[0]))):
        break
    if(lines[fy][fx] == "#"):
        direction = (direction+1)%4
    else:
        player = (fy,fx)

num_spots_obs_causes_loop = 0 
counter = 0
total_squares = (len(lines)+1)*(len(lines[0])+1)

# Only try to add obstacles that block the player's initial path
for i,j in player_path:
    counter+=1
    if(lines[i][j] == "."):
        lines[i][j] = "#"
        num_spots_obs_causes_loop += does_get_stuck_in_loop(lines, player_start_pos) == True
        lines[i][j] = "."
# Output
print(num_spots_obs_causes_loop)

end = perf_counter()
print(f"Time: {(end-start) * 1000:.2f}ms")

# Best time
# 6.2s