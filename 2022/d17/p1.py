f = open("input.txt", "r")
valves = {int(ord(line.split()[1][0])*100 + ord(line.split()[1][1])):(int(line.split()[4][5:].replace(";","")),list(map(lambda x:ord(x[0])*100+ord(x[1]),list(map(lambda x :x.replace(",",""),line.split()[9:])))),{}) for line in f.read().split("\n")}
start = int(ord('A') + ord('A') * 100)
for i in valves:
  queue = [i]
  dist = 0
  for j in range(len(valves)):
    seenBefore = {}
    for k in range(len(queue)):
      current = queue.pop(0)
      if(current in seenBefore):
        continue
      seenBefore[current] = 1
      if(current in valves[i][2]):
        if(dist < valves[i][2][current]):
          valves[i][2][current] = dist 
      else:
        valves[i][2][current] = dist
      for n in valves[current][1]:
        queue.append(n)    
    dist+=1
valves = {val:valves[val] for val in valves if valves[val][0] != 0 or val == start}
valves = {val:(valves[val][0],valves[val][1],valves[val][2],i) for i,val in enumerate(valves)}

open = 2**len(valves)-1
DP = {}
def recurse(valve, time):
  global open
  if(open == 0):
    return 0
  c = (valve,time,open)
  if(c in DP):
    return DP[c]
  maxP = -float('inf')
  for i in valves:
    if(valves[i][0] == 0):
      continue
    isOpenIdentifier = 2**(valves[i][3])
    if((open & isOpenIdentifier) == 0):
      continue
    newTime = time-valves[valve][2][i]-1
    if(newTime > 0):
      pressureReleased = newTime * valves[i][0]
      open ^= isOpenIdentifier
      pressure = pressureReleased + recurse(i,newTime)
      if(pressure > maxP):
        maxP = pressure
      open ^= isOpenIdentifier
  DP[c] = maxP if maxP != -float('inf') else 0
  return DP[c]

print(recurse(start,30))