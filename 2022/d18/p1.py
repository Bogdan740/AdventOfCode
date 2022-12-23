f = open("input.txt", "r")
cubes= [tuple(map(int,k.split(","))) for k in f.read().split("\n")]

totalVisibleSides = 0
droplet = {}
directions = ((-1,0,0), (1,0,0), (0,1,0), (0,-1,0), (0,0,-1), (0,0,1))

for x,y,z in cubes:
  cube = x,y,z
  sidesCovered = 0
  for a,b,c in directions:
    if (x+a,y+b,c+z) in droplet:
      sidesCovered+=1
  totalVisibleSides += (6 - 2*sidesCovered)
  droplet[cube] = 1

print(totalVisibleSides)