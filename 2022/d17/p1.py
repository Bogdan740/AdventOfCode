import time

f = open("sample.txt","r")
jetPattern = list(map(lambda x:-1 if x=='<' else 1,f.read()))

drops =  10
#drops = 1000000000000
toUse = int(drops*1.6)
chamber = [[0 for _ in range(7)] for _ in range(toUse)]
directions = {"<" : -1, ">" : 1}

jet = 0


def placeShape(chamber, shapeID, heightToDropFrom,x):
  if(shapeID == 0):  # TODO use case statement
    chamber[heightToDropFrom][x] = 1
    chamber[heightToDropFrom][x+1] = 1
    chamber[heightToDropFrom][x+2] = 1
    chamber[heightToDropFrom][x+3] = 1
  elif(shapeID == 1): 
    chamber[heightToDropFrom+2][x+1] = 1
    chamber[heightToDropFrom+1][x] = 1
    chamber[heightToDropFrom+1][x+1] = 1
    chamber[heightToDropFrom+1][x+2] = 1
    chamber[heightToDropFrom][x+1] = 1
  elif(shapeID == 2):  
    chamber[heightToDropFrom][x] = 1
    chamber[heightToDropFrom][x+1] = 1
    chamber[heightToDropFrom][x+2] = 1
    chamber[heightToDropFrom+1][x+2] = 1
    chamber[heightToDropFrom+2][x+2]= 1
  elif(shapeID == 3):  
    chamber[heightToDropFrom+3][x] = 1
    chamber[heightToDropFrom+2][x] = 1
    chamber[heightToDropFrom+1][x] = 1
    chamber[heightToDropFrom][x] = 1
  else: 
    chamber[heightToDropFrom+1][x] = 1
    chamber[heightToDropFrom+1][x+1] = 1
    chamber[heightToDropFrom][x] = 1
    chamber[heightToDropFrom][x+1] = 1


def pushShape(chamber, shapeID, sx, sy, pushK = None):
  
  global jet
  global jetPattern
  push = jetPattern[jet]
  jet = (jet + 1) % len(jetPattern)

  if(pushK):
    push = pushK
  if(shapeID == 0):
    if(0 <= sx + push< 7 and ( 
        (push == -1 and chamber[sy][sx-1] != 1) or 
        (push == 1 and sx+4 < 7 and chamber[sy][sx+4] != 1))):
      sx += push
    return sx
  elif(shapeID == 1):
    if(0 <= sx + push< 7 and ( (push == -1 and chamber[sy][sx] != 1 and chamber[sy+2][sx] != 1 and chamber[sy+1][sx-1] != 1) 
      or (push == 1 and sx+3 < 7 and chamber[sy][sx+2] != 1 and chamber[sy+2][sx+2] != 1 and chamber[sy+1][sx+3] != 1))):
      sx += push
    return sx
  elif(shapeID == 2):
    if(0 <= sx + push< 7 
      and ( (push == -1 and chamber[sy][sx-1] != 1 and chamber[sy+1][sx+1] != 1 and chamber[sy+2][sx+1] != 1) 
      or (push == 1 and sx+3 < 7 and chamber[sy][sx+3] != 1 and chamber[sy+1][sx+3] != 1 and chamber[sy+2][sx+3] != 1))):
      sx += push
    return sx
  elif(shapeID == 3):
    if(0 <= sx + push< 7 
      and ( (push == -1  and chamber[sy][sx-1] != 1 and chamber[sy+1][sx-1] != 1 and chamber[sy+2][sx-1] != 1 and chamber[sy+3][sx-1] != 1) 
      or (push == 1 and chamber[sy][sx+1] != 1 and chamber[sy+1][sx+1] != 1 and chamber[sy+2][sx+1] != 1 and chamber[sy+3][sx+1] != 1))):
      sx += push
    return sx
  else:
    if(0 <= sx + push< 7 
      and ( (push == -1 and chamber[sy][sx-1] != 1 and chamber[sy+1][sx-1] != 1) 
      or (push == 1 and sx+2 < 7 and chamber[sy][sx+2] != 1 and chamber[sy+1][sx+2] != 1))):
      sx += push
    return sx



def drop(chamber,shapeID, heightToDropFrom,v = False,t = 0):
  global y
  sx,sy = 2,heightToDropFrom
  # placeShape(chamber,shapeID, sy,sx)
  if(shapeID == 0):
    while(True): 
      if(v):
        time.sleep(t)
        for i in chamber[::-1]:
          print("".join(map(str,i)))
        print("-------")      
      sx = pushShape(chamber, shapeID, sx,sy)
      placed = False
      for j in range(4):
        if(sy - 1 < 0 or chamber[sy-1][sx+j] == 1):
          placed = True
      if(placed):
        break
        
      sy -= 1
    placeShape(chamber,shapeID, sy, sx) 
    y = max(sy,y)
  elif(shapeID == 1):
    while(True):
      if(v):
        time.sleep(t)
        for i in chamber[::-1]:
          print("".join(map(str,i)))
        print("-------")
      sx = pushShape(chamber, shapeID, sx,sy)
      placed = False
      if(sy-1 < 0 or chamber[sy-1][sx+1] == 1 or chamber[sy][sx] == 1 or chamber[sy][sx+2] == 1):
        placed = True
      if(placed):
        break
      
      sy -= 1
    placeShape(chamber,shapeID, sy, sx)
    y = max(sy + 2,y)
  elif(shapeID == 2):
    while(True): 
      if(v):
        time.sleep(t)
        for i in chamber[::-1]:
          print("".join(map(str,i)))
        print("-------")
      sx = pushShape(chamber, shapeID, sx,sy)
      placed = False
      if(sy-1 < 0 or chamber[sy-1][sx] == 1 or chamber[sy-1][sx+1] == 1 or chamber[sy-1][sx+2] == 1):
        placed = True
      if(placed):
        break
      
      sy -= 1
    placeShape(chamber,shapeID, sy, sx)
    y = max(sy + 2,y)
  elif(shapeID == 3):
    while(True):
      if(v):  
        time.sleep(t)
        for i in chamber[::-1]:
          print("".join(map(str,i)))
        print("-------")
      sx = pushShape(chamber, shapeID, sx,sy)
      placed = False
      if(sy-1 < 0 or chamber[sy-1][sx] == 1):
        placed = True
      if(placed):
        break
      
      sy -= 1
    placeShape(chamber,shapeID, sy, sx)
    y = max(sy + 3,y)
  else:
    while(True):
      if(v):  
        time.sleep(t)
        for i in chamber[::-1]:
          print("".join(map(str,i)))
        print("-------")
      sx = pushShape(chamber, shapeID, sx,sy)
      placed = False
      if(sy-1 < 0 or chamber[sy-1][sx] == 1 or chamber[sy-1][sx+1] == 1):
        placed = True
      if(placed):
        break

      sy -= 1
    placeShape(chamber,shapeID, sy, sx)
    y = max(sy+1,y)
  return sx,sy
    
y = -1
DP = {}

heights = [0 for _ in range(7)]
for i in range(drops):
  oldY = y
  a,b = drop(chamber,i%5,y+4, True, 0.5)
  for j in range(7):
    heights[j] = chamber[j].count(1)
  print(heights)
  diffs = (heights[0]-k for k in heights)
  ident = (a, i%5,diffs)
  if(ident in DP):
    print("PATTERN FOUND at iteration : ",i)
    break
  else:
    DP[ident] = 1
  

print(y+1, drops*4)
wastage = ((toUse - y)/(toUse))
print(wastage)

  
  
  
  
