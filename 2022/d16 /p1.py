f = open("sample.txt", "r")
valves = {ord(line.split()[1][1])-65:(int(line.split()[4][5:].replace(";","")),[], list(map(lambda x:ord(x[0])-65,list(map(lambda x :x.replace(",",""),line.split()[9:]))))) for line in f.read().split("\n")}
DP = [[ 0 for _ in range(31)] for _ in range(len(valves))]

for v in valves:
  for k in valves:
    if(v in valves[k][2]):
      valves[v][1].append(k)
    
opened = {valve:False for valve in valves}

for valve in range(len(DP)):
  for minute in range(1,len(DP[0])):
    comeFrom = valves[valve][1] # Valves where we could have come from
    if(opened[valve]):
      arr = [ DP[v][minute-1] for v in comeFrom]
      DP[valve][minute] = max(arr)
    else:
      pressure = valves[valve][0]
      arr = [ DP[v][minute-1] for v in comeFrom]
      DP[valve][minute] = max(max(arr), (30-minute+1) * pressure)

for i in DP:
  print(i)
      
      
    
    