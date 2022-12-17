f = open("sample.txt", "r")

sensBeac = [ [(int(k[2][2:-1]),int(k[3][2:-1])), (int(k[-2][2:-1]),int(k[-1][2:]))] for k in [(line.split()) for line in f.read().split("\n")]]

minX = min(map(lambda x : min(x[0][0],x[1][0]),sensBeac))
maxX = max(map(lambda x : max(x[0][0],x[1][0]),sensBeac))
minY = min(map(lambda x : min(x[0][1],x[1][1]),sensBeac))
maxY = max(map(lambda x : max(x[0][1],x[1][1]),sensBeac))

# Transform everything so that all values are positive
sensBeac = [ [(x -minX, y-minY), (a-minX,b-minY)] for (x,y),(a,b) in sensBeac]
maxX -= minX
maxY -= minY
minX = 0
minY = 0
grid = [['.' for _ in range(minX,maxX+1)] for _ in range(minY,maxY+1)]

for (sx,sy),(bx,by) in sensBeac:
  grid[sy][sx] = "S"
  grid[by][bx] = "B"

def floodOut(start,dist):
  queue = [start]
  nbours = [(0,1), (0,-1), (1,0), (-1,0)]
  for _ in range(dist):
    for _ in range(len(queue)):
      x,y = queue.pop(0)
      if(grid[y][x] == "."):
        grid[y][x] = "#"
      for a,b in nbours:
        nx,ny = x+a,y+b
        if( 0<= ny < len(grid) and 0<= nx < len(grid[0]) and grid[ny][nx] != '#'):
          queue.append((nx,ny))
          
for (sx,sy),(bx,by) in sensBeac:
  dist = abs(sx-bx) + abs(sy-by)
  # print(sx,sy,bx,by,dist,grid[sy][sx])
  floodOut((sx,sy), dist+1)
  
  
for i,g in enumerate(grid):
  print(str(i) + (" " if i < 10 else ""),"".join(g))

print("".join(grid[10]))
print("".join(grid[10]).count("#"))

