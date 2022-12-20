f = open("sample.txt", "r")
valves = {int(str(ord(line.split()[1][0])) + str(ord(line.split()[1][1]))):(int(line.split()[4][5:].replace(";","")),list(map(lambda x:int(str(ord(x[0]))+str(ord(x[1]))),list(map(lambda x :x.replace(",",""),line.split()[9:])))),{}) for line in f.read().split("\n")}
counter = 0
for i in valves:
  valves[i] = (valves[i][0],valves[i][1],valves[i][2],counter)
  counter+=1

first = None
for i in valves:
  first = i
  break

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
        valves[i][2][current] = dist if dist < valves[i][2][current] else valves[i][2][current]
      else:
        valves[i][2][current] = dist
        
      for n in valves[current][1]:
        queue.append(n)    
    dist+=1

open = 2**len(valves)-1
counter = 0
DP = {}
def recurse(valve, time):
  global open
  if(open == 0):
    print("DIBE")
    return 0
  c = (valve,time,open)
  if(c in DP):
    return DP[c]
  maxP = -float('inf')
  for i in valves:
    isOpenIdentifier = 2**valves[i][3]
    if(open & isOpenIdentifier== 0):
      continue
    dist = valves[valve][2][i]
    timePenalty = dist + 1
    newTime = time-timePenalty
    if(newTime > 0):
      pressureReleased = newTime * valves[i][0]
      open ^= isOpenIdentifier
      pressure = pressureReleased + recurse(i,newTime)
      if(pressure > maxP):
        maxP = pressure
      open ^= isOpenIdentifier
  DP[c] = maxP if maxP != -float('inf') else 0
  return DP[c]


print(recurse(first, 30))
    
# 16 - 4.5 - 4.6 seconds 
