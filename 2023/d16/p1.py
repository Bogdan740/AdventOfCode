from time import perf_counter

t1 = perf_counter()

lines = None
with open("input.txt", "r") as fp:
    lines = fp.read().split("\n")
    
grid = [list(line) for line in lines]

UP, RIGHT, DOWN, LEFT = 0,1,2,3
move_dir = {UP : (0,-1), RIGHT : (1,0), DOWN : (0,1), LEFT : (-1,0)}
mirrors = {
    "/" : {RIGHT : UP, LEFT : DOWN, UP : RIGHT, DOWN : LEFT},
    "\\" : {RIGHT : DOWN, DOWN : RIGHT, LEFT : UP, UP : LEFT}
    }
splitters = {
    "-" : {UP : (LEFT, RIGHT), DOWN : (LEFT, RIGHT), LEFT : (LEFT, -1), RIGHT : (RIGHT, -1)}, 
    "|" : {UP : (UP, -1), DOWN : (DOWN, -1), LEFT : (UP, DOWN), RIGHT : (UP, DOWN)}
    }

beams = [(-1,0,RIGHT)]
seen_before_beams = set()
en = set()
while(len(beams) != 0):
    beams = [beam for beam in beams if beam != -1 and beam not in seen_before_beams]
    for i,beam in enumerate(beams):
        seen_before_beams.add(beam)
        x,y,direction = beam
        en.add((x,y))
        move_x, move_y = move_dir[direction]
        nx,ny = x+move_x, y+move_y
        if(not (0 <= nx < len(grid[0]) and 0 <= ny < len(grid))):
            beams[i] = -1
            continue
        val = grid[ny][nx]
        if(val == "."):
            beams[i] = (nx,ny,direction)
        if(val == "/" or val == "\\"):
            new_dir = mirrors[val][direction]
            beams[i] = (nx, ny, new_dir)
        elif(val == "|" or val  == "-"):
            new_dir_1, new_dir_2 = splitters[val][direction]
            beams[i] = (nx, ny, new_dir_1)
            if(new_dir_2 != -1):
                beams.append((nx,ny, new_dir_2))

print(len(en)-1)

t2 = perf_counter()
print(f"Time : {(t2-t1)*1000:.2f}ms")