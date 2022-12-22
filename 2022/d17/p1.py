import time

f = open("sample.txt","r")

jetPattern = f.read()
jet = 0
# shapes = {0 :["####"], 1 : [".#.", "###", ".#."], 2 : ["..#","..#","###"], 3: ["#","#","#","#"], 4 :["##","##"] }
chamber = [["." for _ in range(7)] for _ in range(4*2022)]

directions = {"<" : -1, ">" : 1}
def nextJet():
  global jet
  global jetPattern
  toReturn = jetPattern[jet]
  jet = (jet + 1) % len(jetPattern)
  return directions[toReturn]
def placeShape(chamber, shapeID, heightToDropFrom,x):
  if(shapeID == 0):  # TODO use case statement
    chamber[heightToDropFrom][x] = "#"
    chamber[heightToDropFrom][x+1] = "#"
    chamber[heightToDropFrom][x+2] = "#"
    chamber[heightToDropFrom][x+3] = "#"
  if(shapeID == 1): 
    chamber[heightToDropFrom+2][x+1] = "#"
    chamber[heightToDropFrom+1][x] = "#"
    chamber[heightToDropFrom+1][x+1] = "#"
    chamber[heightToDropFrom+1][x+2] = "#"
    chamber[heightToDropFrom][x+1] = "#"
  if(shapeID == 2):  
    chamber[heightToDropFrom][x] = "#"
    chamber[heightToDropFrom][x+1] = "#"
    chamber[heightToDropFrom][x+2] = "#"
    chamber[heightToDropFrom+1][x+2] = "#"
    chamber[heightToDropFrom+2][x+2]= "#"
  if(shapeID == 3):  
    chamber[heightToDropFrom+3][x] = "#"
    chamber[heightToDropFrom+2][x] = "#"
    chamber[heightToDropFrom+1][x] = "#"
    chamber[heightToDropFrom][x] = "#"
  if(shapeID == 4): 
    chamber[heightToDropFrom+1][x] = "#"
    chamber[heightToDropFrom+1][x+1] = "#"
    chamber[heightToDropFrom][x] = "#"
    chamber[heightToDropFrom][x+1] = "#"
    
def pushShape(chamber, shapeID,x,y,direction):
  if(shapeID == 0):
    for i in range(4):
      chamber[y][x+i] = "."
    for i in range(4):
      chamber[y][x+i+direction] = "#"
  elif(shapeID == 1):
    chamber[y][x+1] = "."
    chamber[y-1][x] = "."
    chamber[y-1][x+1] = "."
    chamber[y-1][x+2] = "."
    chamber[y-2][x+1] = "."
    
    chamber[y][x+1+direction] = "#"
    chamber[y-1][x+direction] = "#"
    chamber[y-1][x+1+direction] = "#"
    chamber[y-1][x+2+direction] = "#"
    chamber[y-2][x+1+direction] = "#"
  elif(shapeID == 2):
    chamber[y][x] = "."
    chamber[y][x+1] = "."
    chamber[y][x+2] = "."
    chamber[y+1][x+2] = "."
    chamber[y+2][x+2]= "."
    
    chamber[y][x+direction] = "#"
    chamber[y][x+1+direction] = "#"
    chamber[y][x+2+direction] = "#"
    chamber[y+1][x+2+direction] = "#"
    chamber[y+2][x+2+direction]= "#"
  elif(shapeID == 3):
    chamber[y+3][x] = "."
    chamber[y+2][x] = "."
    chamber[y+1][x] = "."
    chamber[y][x] = "."
    
    chamber[y+3][x+direction] = "#"
    chamber[y+2][x+direction] = "#"
    chamber[y+1][x+direction] = "#"
    chamber[y][x+direction] = "#"
  elif(shapeID == 4):
    chamber[y+1][x] = "."
    chamber[y+1][x+1] = "."
    chamber[y][x] = "."
    chamber[y][x+1] = "."
    
    chamber[y+1][x+direction] = "#"
    chamber[y+1][x+1+direction] = "#"
    chamber[y][x+direction] = "#"
    chamber[y][x+1+direction] = "#"
    
  


def pushTing(chamber, shapeID, sx, sy, pushK = None):
  push = nextJet()
  if(pushK):
    push = pushK
  if(shapeID == 0):
    if(0 <= sx + push< 7 and ( 
        (push == -1 and chamber[sy][sx+push] != '#' and chamber[sy+1][sx] != '#' and chamber[sy-1][sx] != '#') or 
        (push == 1 and sx+push+3 < 7 and chamber[sy][sx+push+3] != '#' and chamber[sy-1][sx+push+2] != '#' and chamber[sy+1][sx+push+2] != '#'))):
      pushShape(chamber, shapeID, sx,sy, push)
      sx += push
    return sx
  if(shapeID == 1):
    if(0 <= sx + push< 7 and ( (push == -1 and chamber[sy][sx+push] != '#') or (push == 1 and sx+push+2 < 7 and chamber[sy][sx+push+2] != '#'))):
      pushShape(chamber, shapeID, sx,sy, push)
      sx += push
    return sx
  if(shapeID == 2):
    if(0 <= sx + push< 7 
      and ( (push == -1 and chamber[sy][sx+push] != '#' and sx+1 < 7 and chamber[sy+1][sx+1] != '#' and chamber[sy+2][sx+1] != '#') 
      or (push == 1 and sx+3 < 7 and chamber[sy][sx+3] != '#' and chamber[sy+1][sx+3] != '#' and chamber[sy+2][sx+3] != '#'))):
      pushShape(chamber, shapeID, sx,sy, push)
      sx += push
    return sx
  if(shapeID == 3):
    if(0 <= sx + push< 7 
      and ( (push == -1 and sx - 1 >= 0 and chamber[sy][sx-1] != '#' and chamber[sy+1][sx-1] != '#' and chamber[sy+2][sx-1] != '#' and chamber[sy+3][sx-1] != '#') 
      or (push == 1 and sx+1 < 7 and chamber[sy][sx+1] != '#' and chamber[sy+1][sx+1] != '#' and chamber[sy+2][sx+1] != '#' and chamber[sy+3][sx+1] != '#'))):
      pushShape(chamber, shapeID, sx,sy, push)
      sx += push
    return sx
  if(shapeID == 4):
    if(0 <= sx + push< 7 
      and ( (push == -1 and sx - 1 >= 0 and chamber[sy][sx-1] != '#' and chamber[sy+1][sx-1] != '#') 
      or (push == 1 and sx+2 < 7 and chamber[sy][sx+2] != '#' and chamber[sy+1][sx+2] != '#'))):
      pushShape(chamber, shapeID, sx,sy, push)
      sx += push
    return sx



def drop(chamber,shapeID, heightToDropFrom,v = False,t = 0):
  global y
  sx,sy = 2,heightToDropFrom
  placeShape(chamber,shapeID, sy,sx)
  if(shapeID == 0):
    while(True): 
      if(v):
        time.sleep(t)
        for i in chamber[::-1]:
          print("".join(i))
        print("-------")      
      sx = pushTing(chamber, shapeID, sx,sy)
      placed = False
      for j in range(4):
        if(sy - 1 < 0 or chamber[sy-1][sx+j] == "#"):
          placed = True
      if(placed):
        break
      for j in range(4):
        chamber[sy][sx+j] = "."
        placeShape(chamber,shapeID, sy-1, sx)
        
      sy -= 1
    y = max(sy,y)
  if(shapeID == 1):
    while(True):
      if(v):
        time.sleep(t)
        for i in chamber[::-1]:
          print("".join(i))
        print("-------")
      sx = pushTing(chamber, shapeID, sx,sy+2)
      placed = False
      if(sy-1 < 0 or chamber[sy-1][sx+1] == "#" or chamber[sy][sx] == "#" or chamber[sy][sx+2] == "#"):
        placed = True
      if(placed):
        break
      chamber[sy][sx+1] = "."
      chamber[sy+1][sx] = "."
      chamber[sy+1][sx+1] = "."
      chamber[sy+1][sx+2] = "."
      chamber[sy+2][sx+1] = "."
      placeShape(chamber,shapeID, sy-1, sx)
      
      sy -= 1
    y = max(sy + 2,y)
  if(shapeID == 2):
    while(True): 
      if(v):
        time.sleep(t)
        for i in chamber[::-1]:
          print("".join(i))
        print("-------")
      sx = pushTing(chamber, shapeID, sx,sy)
      placed = False
      if(sy-1 < 0 or chamber[sy-1][sx] == "#" or chamber[sy-1][sx+1] == "#" or chamber[sy-1][sx+2] == "#"):
        placed = True
      if(placed):
        break
      chamber[sy][sx] = "."
      chamber[sy][sx+1] = "."
      chamber[sy][sx+2] = "."
      chamber[sy+1][sx+2] = "."
      chamber[sy+2][sx+2]= "."
      placeShape(chamber,shapeID, sy-1, sx)
      
      sy -= 1
    y = max(sy + 2,y)
  if(shapeID == 3):
    while(True):
      if(v):  
        time.sleep(t)
        for i in chamber[::-1]:
          print("".join(i))
        print("-------")
      sx = pushTing(chamber, shapeID, sx,sy)
      placed = False
      if(sy-1 < 0 or chamber[sy-1][sx] == "#"):
        placed = True
      if(placed):
        break
      chamber[sy][sx] = "."
      chamber[sy+1][sx] = "."
      chamber[sy+2][sx] = "."
      chamber[sy+3][sx] = "."
      placeShape(chamber,shapeID, sy-1, sx)
      
      sy -= 1
    y = max(sy + 3,y)
  if(shapeID == 4):
    while(True):
      if(v):  
        time.sleep(t)
        for i in chamber[::-1]:
          print("".join(i))
        print("-------")
      sx = pushTing(chamber, shapeID, sx,sy)
      placed = False
      if(sy-1 < 0 or chamber[sy-1][sx] == "#" or chamber[sy-1][sx+1] == "#"):
        placed = True
      if(placed):
        break
      chamber[sy+1][sx] = "."
      chamber[sy+1][sx+1] = "."
      chamber[sy][sx] = "."
      chamber[sy][sx+1] = "."
      placeShape(chamber,shapeID, sy-1, sx)
      
      sy -= 1
    y = max(sy+1,y)
    
y = -1
for i in range(2022):
  drop(chamber,i%5,y+4)

print(y)
# time.sleep(1)
# for i in chamber[::-1]:
#   print("".join(i))
# print("-------")
  
  
  
  
  
