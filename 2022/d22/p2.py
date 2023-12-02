f = open("sample2.txt", "r")
parsed = f.read().split("\n")

grid = list(map(lambda x:x.replace(" ","x"),parsed[:-2]))
maxWidth = max(map(len,grid))
grid = [list(x) + ["x"]*(maxWidth-len(x)) for x in grid]

l = 4

# def rotateClockwise(arr):
#   return list(zip(*arr[::-1]))

# face6 = [s[2*l:3*l] for s in grid[:l]]
# face3 = [s[:l] for s in grid[3*l:4*l]]
# face2 = [s[:l] for s in grid[2*l:3*l]]

# rotatedFace6 = rotateClockwise(rotateClockwise(face6))
# rotatedFace2 = rotateClockwise(face2)
# rotatedFace3 = rotateClockwise(face3)


# grid = list(map(lambda x:["x"]*l + x,grid))[:-l]

# for i in range(l):
#   grid[i] = grid[i][:-l] + ["x"] * l
#   grid[-(i+1)] =  ["x"] * 2*l + grid[-(i+1)][2*l:]
#   grid[-(l+i+1)] = ["x"] * 2*l + grid[-(l+i+1)][2*l:]
# for i in range(l):
#   grid[l+i] = list(rotatedFace2[i]) + list(rotatedFace3[i]) + grid[l+i][2*l:3*l] + ["x"]*l
#   grid[2*l+i] =  ["x"] * 2*l + grid[2*l+i][2*l:3*l] + list(rotatedFace6[i])
  
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

RIGHT = 0
DOWN = 1
LEFT = 2
UP = 3

turn = {"R" : 1, "L" : -1 }
movements = {RIGHT : (1,0), DOWN : (0,1), LEFT : (-1,0), UP: (0,-1) }
drawDir = {RIGHT : ">",DOWN : "v" ,LEFT : "<" ,UP : "^"}
cx,cy = grid[0].index("."),0 
currentDirection = RIGHT # RIGHT
WALL = "#"
WARP = "x"

lastDir = None

for i in grid:
  print("".join(i))
for i in instructions:
  if(type(i) == int):
    # Move forward i steps
    for _ in range(i):
      grid[cy][cx] = drawDir[currentDirection]
      dx,dy = movements[currentDirection]
      nx,ny = cx + dx, cy + dy
      if( not 0 <= nx < len(grid[0]) or not 0 <= ny < len(grid) or grid[ny][nx] == WARP):
        if(0 <= ny < l and nx == 2*l -1 and currentDirection == LEFT):# Going off the left side of face 1, onto the top side of face 3
          nx = l + ny
          ny = l
          currentDirection = DOWN
        elif(ny == l-1 and l <= nx < 2*l and currentDirection == UP): # Going off the top of face 3, onto the left side of face 1
          ny = nx - l
          nx = 2*l
          currentDirection = RIGHT
          
        elif(0 <= ny < l and nx == 3*l and currentDirection == RIGHT):# Going off the right side of face 1, onto the right side of face 6
          ny = 2*l + (l-(ny+1))
          nx = 4*l -1
          currentDirection =LEFT
        elif(2*l <= ny < 3*l and nx == 4*l and currentDirection == RIGHT):# Going off the right side of face 6, onto the right of face 1
          ny = (3*l - ny) - 1
          nx = 3*l -1
          currentDirection =LEFT
          
        elif( nx == -1 and l <= ny < 2*l and currentDirection == LEFT): # Going off the left side of face 2, onto the bottom side of face 6
          nx = 3*l + (l - (ny - l)) - 1
          ny = 3*l -1
          currentDirection = UP
        elif( 3*l <= nx < 4*l and ny == 3*l and currentDirection == DOWN): # Going off the bottom side of face 6, onto the left side of face 2
          ny = 3*l + (l - (nx - l)) - 1
          nx = 0
          currentDirection = RIGHT
        
        elif(nx == 2*l-1 and 2*l <= ny < 3*l and currentDirection == LEFT): # Going off the left side of face 5, onto the bottom side of face 3
          nx = l + (3*l-ny - 1)
          ny = 2*l -1
          currentDirection = UP
        elif(l <= nx < 2*l and ny == 2*l and currentDirection == DOWN): # Going off the bottom side of face 3, onto the left side of face 5
          ny = 3*l - (nx - l) - 1 
          nx = 2*l 
          currentDirection = RIGHT
        
        elif(0 <= nx < l and ny == l-1 and currentDirection == UP): # Going off the top side of face 2, onto the top side of face 1
          nx = 3*l - 1 - nx 
          ny = 0 
          currentDirection = DOWN
        elif(2*l <= nx < 3*l and ny == -1 and currentDirection == UP): # Going off the top side of face 1, onto the top side of face 2
          nx = l - (nx-2*l) - 1
          ny = l 
          currentDirection = DOWN
            
        
        elif(0 <= nx < l and ny == 2*l and currentDirection == DOWN): # Going off the bottom side of face 2, onto the bottom side of face 5
          nx = 3*l - nx - 1
          ny = 3*l - 1
          currentDirection = UP
        elif(2*l <= nx < 3*l and ny == 3*l and currentDirection == DOWN): # Going off the bottom side of face 5, onto the bottom side of face 2
          nx = 3*l - nx - 1
          ny = 2*l - 1
          currentDirection = UP

        elif(nx == 3*l and l <= ny < 2*l and currentDirection == RIGHT): # Going off the right side of face 4, onto the top side of face 6
          nx = 4*l - (ny - l) - 1
          ny = 2*l
          currentDirection = DOWN
        elif(3*l <= nx < 4*l and ny == 2*l-1 and currentDirection == UP): # Going off the top side of face 6, onto the right side of face 4
          ny = 2*l - (nx - 3*l) -1
          nx = 3*l-1
          currentDirection = LEFT
      if(grid[ny][nx] == WALL):
        break
      grid[ny][nx] = drawDir[currentDirection]
      cy,cx = ny,nx
  else:
    # Set current direction to new direction
    currentDirection = (currentDirection + turn[i])%4
    lastDir = currentDirection

row = cy+1
column = cx + 1
facing = lastDir

grid[cy][cx] = "E"

print(row,column, facing)
print(1000*row + 4 * column + facing)

for i in grid:
  print("".join(i))
# tried : 11454, 115676 