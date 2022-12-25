f = open("input.txt", "r")
parsed = f.read().split("\n")

grid = list(map(lambda x:x.replace(" ","x"),parsed[:-1]))
maxWidth = max(map(len,grid))
grid = [list(x) + ["x"]*(maxWidth-len(x)) for x in grid]

instructionsUnparsed = parsed[-1]
instructions = []

buffer = ""
for i in instructionsUnparsed:
  if i.isnumeric():
    buffer+=i
  else:
    instructions.append(int(buffer))
    instructions.append(i)
    buffer = ""
instructions.append(int(buffer))

turn = {"R" : 1, "L" : -1 }
movements = {0 : (1,0), 1 : (0,1), 2 : (-1,0), 3: (0,-1) }

cx,cy = grid[0].index("."),0 
currentDirection = 0 # RIGHT
WALL = "#"
WARP = "x"

for i in instructions:
  if(type(i) == int):
    # Move forward i steps
    dx,dy = movements[currentDirection]
    for _ in range(i):
      nx,ny = (cx + dx)%len(grid[0]), (cy + dy) % len(grid)
      while(grid[ny][nx] == WARP):
        nx,ny = (nx + dx)%len(grid[0]), (ny + dy) % len(grid)
      if(grid[ny][nx] == WALL):
        break
      cy,cx = ny,nx
      grid[cy][cx] = "!"
  else:
    # Set current direction to new direction
    currentDirection = (currentDirection + turn[i])%4

row = cy+1
column = cx + 1
facing = currentDirection
print(1000*row + 4 * column + 0)