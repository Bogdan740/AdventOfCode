f = open("input.txt", "r")

# Assumes that length and width of forest are the same (It's square shaped)
inp = f.read()
rows = [list(map(int,list(i))) for i in inp.split('\n')]
cols = [ [] for i in range(len(rows[0]))]

for row in rows:
  for i,col in enumerate(row):
    cols[i].append(col)
    
canBeSeen = [ [False for _ in range(len(rows[0]))] for _ in range(len(rows))]
canBeSeenCounter = 0

def treesVisible(row,x,reversedX = False, reversedY = False):
  canBeSeenCounter = 0
  maxHeight = -1
  for y,val in enumerate(row):
    yVal = y if not reversedX else len(row)-y-1
    if(val > maxHeight):
      maxHeight = val
      if( (not canBeSeen[x][yVal] and not reversedY)):
        canBeSeenCounter += 1
        canBeSeen[x][yVal] = True
      elif((not canBeSeen[yVal][x] and reversedY)):
        canBeSeenCounter += 1
        canBeSeen[yVal][x] = True
  return canBeSeenCounter

  
for x,row in enumerate(rows):
  canBeSeenCounter += treesVisible(row,x)  + treesVisible(row[::-1],x,True)
for x,col in enumerate(cols):
  canBeSeenCounter += treesVisible(col,x,False, True)  + treesVisible(col[::-1],x, True, True)

print(canBeSeenCounter)