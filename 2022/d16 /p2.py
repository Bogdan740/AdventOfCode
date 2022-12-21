f = open("input.txt", "r")
valves = {int(ord(line.split()[1][0])*100 + ord(line.split()[1][1])):(int(line.split()[4][5:].replace(";","")),list(map(lambda x:ord(x[0])*100+ord(x[1]),list(map(lambda x :x.replace(",",""),line.split()[9:])))),{},i) for i,line in enumerate(f.read().split("\n"))}
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
    
def sublists(xs):
  l = len(xs)
  for i in range(1 << l):
      incl, excl = [], []
      for j in range(l):
          if i & (1 << j):
              incl.append(xs[j])
          else:
              excl.append(xs[j])
      yield (incl,excl)
  
def recurse(valve, time, allowed):
  global open
  if(open == 0):
    return 0
  c = (valve,time,open)
  if(c in DP):
    return DP[c]
  maxP = -float('inf')
  for i in allowed:
    if(valves[i][0] == 0):
      continue
    isOpenIdentifier = 2**allowed[i]
    if((open & isOpenIdentifier) == 0):
      continue
    newTime = time-valves[valve][2][i]-1
    if(newTime > 0):
      pressureReleased = newTime * valves[i][0]
      open ^= isOpenIdentifier
      pressure = pressureReleased + recurse(i,newTime,allowed)
      if(pressure > maxP):
        maxP = pressure
      open ^= isOpenIdentifier
  DP[c] = maxP if maxP != -float('inf') else 0
  return DP[c]

splits = list(sublists([i for i in valves if valves[i][0]!=0]))
splits = splits[:len(splits)//2]
maxP = -float('inf')


for i,(x,y) in enumerate(splits):
  x+=[start];y+=[start]
  p = 0
  DP = {}
  open = 2**(len(x)+1)-1
  allowed1 = {val:i for i,val in enumerate(x) } 
  p += recurse(start,26, allowed1)
  DP = {}
  open = 2**(len(y)+1)-1
  allowed2 = {val:i for i,val in enumerate(y)}
  p += recurse(start,26, allowed2)
  if(p > maxP):
    maxP = p

print(maxP)