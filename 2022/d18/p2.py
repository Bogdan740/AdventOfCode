f = open("input.txt", "r")
cubes= [tuple(map(int,k.split(","))) for k in f.read().split("\n")]

droplet = {}
directions = ((-1,0,0), (1,0,0), (0,1,0), (0,-1,0), (0,0,-1), (0,0,1))
minX,maxX,minY,maxY,minZ,maxZ = [float('inf'),-float('inf'),float('inf'),-float('inf'),float('inf'),-float('inf')]
for x,y,z in cubes:
  if(x < minX):minX =x
  elif(x > maxX):maxX = x
  if(y < minY):minY =y
  elif(y > maxY):maxY = y
  if(z < minZ):minZ =z
  elif(z > maxZ):maxZ = z
  
  cube = x,y,z
  droplet[cube] = 1

# Floodfill algorithm
minX-=1;maxX+=1;minY-=1;maxY+=1;minZ-=1;maxZ+=1
totalVisibleSides = 0
seenBefore = {}
queue = [(minX,minY,minZ)]
while(len(queue) != 0):
  for _ in range(len(queue)):
    cx,cy,cz = queue.pop(0)
    for dx,dy,dz in directions:
      nx,ny,nz = cx+dx,cy+dy,cz+dz
      if(minX <= nx <= maxX and minY <= ny <= maxY and minZ <= nz <= maxZ and cube):
        cube = (nx,ny,nz)
        if(cube in droplet):
          totalVisibleSides +=1
        elif(cube not in droplet and cube not in seenBefore):
          queue.append(cube)
          seenBefore[cube] =1 
        
        
      


print(totalVisibleSides)
