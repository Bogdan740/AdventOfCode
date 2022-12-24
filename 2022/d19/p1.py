f = open("input.txt", "r")
blueprints= [ list(map(lambda x:x.split()[4:],line.split(":")[1].split(".")))[:-1] for line in f.read().split("\n")]

for bp in blueprints:
  bp[0] = int(bp[0][0])
  bp[1] = int(bp[1][0])
  bp[2] = [int(bp[2][0]),int(bp[2][-2])]
  bp[3] = [int(bp[3][0]),int(bp[3][-2])]

 # line format : | ore robot : [4 ore] | clay robot : [2 ore] | Obsidian robot : [3 ore, 14 clay] | geode robot : [2 ore, 7 obsidian]

def recurse(bp,oreRob=1,clayRob=0,obsRob=0,geodeRobot=0, ore=0,clay=0,obs=0,geodes=0, time=24):
  if(time == 0):
    return geodes
  c = (oreRob,clayRob,obsRob,geodeRobot, ore,clay,obs,geodes, time)
  if(c in DP):
    return DP[c]
  oreCostOre,oreCostClay ,(oreCostObs ,clayCostObs),(oreCostGeode,obsCostGeode) = bp

  maxGeodes = -float('inf')
  a = recurse(bp,oreRob ,clayRob, obsRob,geodeRobot, ore + oreRob, clay + clayRob, obs + obsRob,geodes + geodeRobot, time-1)
  if(a > maxGeodes):maxGeodes = a
  if(ore >= oreCostOre):
    a = recurse(bp,oreRob + 1,clayRob, obsRob,geodeRobot, ore-oreCostOre + oreRob, clay + clayRob, obs + obsRob,geodes + geodeRobot, time-1)
    if(a > maxGeodes):
        maxGeodes = a
  if(ore >= oreCostClay):
    a = recurse(bp,oreRob,clayRob + 1, obsRob,geodeRobot, ore-oreCostClay + oreRob, clay + clayRob, obs + obsRob,geodes + geodeRobot, time-1)
    if(a > maxGeodes):
      maxGeodes = a
  if(ore >=oreCostObs and clay >=  clayCostObs):
    a = recurse(bp,oreRob,clayRob, obsRob+1,geodeRobot, ore-oreCostObs + oreRob, clay-clayCostObs + clayRob,obs + obsRob,geodes + geodeRobot, time-1)
    if(a > maxGeodes):
      maxGeodes = a
  if(ore >=oreCostGeode and obs >=  obsCostGeode):
    a = recurse(bp,oreRob,clayRob, obsRob,geodeRobot+1, ore-oreCostGeode + oreRob, clay + clayRob,obs - obsCostGeode+ obsRob,geodes + geodeRobot, time-1)
    if(a > maxGeodes):
      maxGeodes = a
  
  DP[c] = maxGeodes
  return maxGeodes

DP = {}

totalScore = 0
counter = 1
for bp in blueprints:
  DP = {}
  rec = recurse(bp)
  print(counter,rec)
  totalScore += rec * counter
  counter+=1

print(totalScore)
  
  
  