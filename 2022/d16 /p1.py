f = open("sample.txt", "r")
valves = {ord(line.split()[1][1])-65:(int(line.split()[4][5:].replace(";","")),list(map(lambda x:ord(x[0])-65,list(map(lambda x :x.replace(",",""),line.split()[9:]))))) for line in f.read().split("\n")}

def distanceFromTo(fromV, toV, valves):
  queue = [fromV]
  dist = 0
  while(len(queue) !=0):
    for _ in range(len(queue)):
      current = queue.pop(0)
      if(current == toV):
        return dist
      for n in valves[current][1]:
        queue.append(n)    
    dist+=1

closed = [valve for valve in valves]
current = 0 # Set our position to AA
time = 30
totalP = 0
while(time >= 0):
  maxP = -float('inf')
  chosen = None
  timePenalty = 0
  for i in closed:
    dist = distanceFromTo(current,i,valves)
    if(time - dist - 1 > 0):
      pressureReleased = (time-dist-1) * valves[i][0]
      if(pressureReleased > maxP):
        maxP = pressureReleased
        chosen = i
        timePenalty = dist + 1
  if(chosen == None):
    break
  time -=timePenalty
  totalP += maxP
  current = chosen
  print(chosen)
  closed.remove(chosen)

print(totalP)
  
    
    
  
  
  
    
