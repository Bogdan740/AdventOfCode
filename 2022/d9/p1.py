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
  # If the tail is diagonally displaced from the head - Move towards the head in two orthogonal directions simultaneously
  j += 1 if (y-j) > 0 else 0 if y-j == 0 else -1
  i += 1 if (x-i) > 0 else 0 if x-i == 0 else -1
  return (i,j)
  
h,t= (0,0),(0,0) # Initiate head and tail at 0,0

seenBefore = {t : 1}
squaresBeenTo = 1
  
for dirLetter,mag in parsed:
  dirs = {"R" : (1,0), "L" : (-1,0), "U" : (0,1), "D": (0,-1) }
  dir = dirs[dirLetter]
  mag = int(mag)
  for _ in range(mag):
    h = (h[0] + dir[0], h[1] + dir[1])
    t = move_tail(h,t) 
    # print(t,h)
    if(t not in seenBefore):
      squaresBeenTo +=1
      seenBefore[t] = 1

print(squaresBeenTo)
