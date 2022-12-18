f = open("input.txt", "r")

sensBeac = [ [(int(k[2][2:-1]),int(k[3][2:-1])), (int(k[-2][2:-1]),int(k[-1][2:]))] for k in [(line.split()) for line in f.read().split("\n")]]

row = 2000000

taken = {}
for (sx,sy),(bx,by) in sensBeac:
  if(sy == row):
    taken[sx] = 1
  if(by == row):
    taken[bx] = 1
def odd(x):
  return 2*x + 1
  
onLine = {}
for (sx,sy),(bx,by) in sensBeac:
  distSB = abs(sx - bx) + abs(sy-by)
  distSR = abs(sy - row)
  if(distSB >= distSR):
    diff = odd(distSB - distSR)
    for x in range(sx-(diff//2),sx+(diff//2)+1):
      if(x not in onLine and x not in taken):
        onLine[x] = 1

print(len(onLine))
