from math import sqrt

f = open("input.txt", "r")

inp = f.read()
parsed = [i.split(" ") for i in inp.split("\n")]

def move_tail(h,t):
  x,y = h
  i,j = t
  dist = sqrt(((x - i) ** 2) + ((y - j) **2))
  # If tail is already touching the head then return the current pos of the tail
  if(dist < 2):
    return t
  # Else, move towards the tail
  j += 1 if (y-j) > 0 else 0 if y-j == 0 else -1
  i += 1 if (x-i) > 0 else 0 if x-i == 0 else -1
  return (i,j)
  
h= (0,0) # Initiate head to (0,0)
tails = [(0,0) for _ in range(9)] # Head <- Tail[0] <- Tail[1] <- ... <- Tail[8]

seenBefore = {tails[-1] : 1}
squaresBeenTo = 1
  
for dirLetter,mag in parsed:
  dirs = {"R" : (1,0), "L" : (-1,0), "U" : (0,1), "D": (0,-1) }
  dir = dirs[dirLetter]
  mag = int(mag)
  for _ in range(mag):
    h = (h[0] + dir[0], h[1] + dir[1])
    tails[0] = move_tail(h,tails[0])
    
    for i in range(1,len(tails)):
      tails[i] = move_tail(tails[i-1],tails[i])
      
    if(tails[-1] not in seenBefore): # tails[-1] is the very end tail
      squaresBeenTo +=1
      seenBefore[tails[-1]] = 1

print(squaresBeenTo)
