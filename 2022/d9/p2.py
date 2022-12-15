f = open("input.txt", "r")

# Assumes that length and width of forest are the same (It's square shaped)
inp = f.read()
rows = [list(map(int,list(i))) for i in inp.split('\n')]

maxScenicScore = 0

for i,row in enumerate(rows):
  for j,tree in enumerate(row):
    directions = [(-1,0), (1,0), (0,-1), (0,1)] # UP, DOWN, LEFT, RIGHT
    scenicScores = [0,0,0,0] # Scenic scores for directions UP, DOWN, LEFT, RIGHT
    for pointer,(ai,aj) in enumerate(directions):
      x,y = i + ai, j+aj
      while(0 <= x < len(rows) and 0 <= y < len(rows[0])):
        scenicScores[pointer]+=1
        if(tree <= rows[x][y]): break
        x,y = x + ai, y+aj
        
    scenicScore = scenicScores[0] * scenicScores[1] * scenicScores[2] * scenicScores[3]
    if(scenicScore > maxScenicScore):
      maxScenicScore = scenicScore
print(maxScenicScore)