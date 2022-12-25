f = open("input.txt", "r")
blueprints= [ list(map(lambda x:x.split()[4:],line.split(":")[1].split(".")))[:-1] for line in f.read().split("\n")]

for i,bp in enumerate(blueprints):
  holder = []
  holder.append(int(bp[0][0]))
  holder.append(int(bp[1][0]))
  holder += [int(bp[2][0]),int(bp[2][-2])]
  holder += [int(bp[3][0]),int(bp[3][-2])]
  blueprints[i] = holder


 # line format : | ore robot : [4 ore] | clay robot : [2 ore] | Obsidian robot : [3 ore, 14 clay] | geode robot : [2 ore, 7 obsidian]

DP = {}

def recurse(bp,oreRob=1, clayRob=0, obsRob=0, geodeRobot=0,  ore=0, clay=0, obs=0, geodes=0, time=31):
  if(time == 0):
    return geodes
  c = (oreRob,clayRob,obsRob,geodeRobot, ore,clay,obs,geodes, time)
  if(c in DP):
    return DP[c]
  oreCostOre,oreCostClay, oreCostObs,clayCostObs, oreCostGeode, obsCostGeode = bp

  maxGeodes = recurse(bp,oreRob ,clayRob, obsRob,geodeRobot, ore + oreRob, clay + clayRob, obs + obsRob,geodes + geodeRobot, time-1)
  # if(oreCostOre <= time and (oreCostGeode <= time or obsCostGeode <= time) and (oreCostObs <= time or clayCostObs <= time) and oreCostClay <= time):
  if(ore >= oreCostOre and oreCostOre <= time ):
    a = recurse(bp,oreRob + 1,clayRob, obsRob,geodeRobot, ore-oreCostOre + oreRob, clay + clayRob, obs + obsRob,geodes + geodeRobot, time-1)
    if(a > maxGeodes):
        maxGeodes = a
  if(ore >= oreCostClay and oreCostClay <= time):
    a = recurse(bp,oreRob,clayRob + 1, obsRob,geodeRobot, ore-oreCostClay + oreRob, clay + clayRob, obs + obsRob,geodes + geodeRobot, time-1)
    if(a > maxGeodes):
      maxGeodes = a
  if(ore >=oreCostGeode and obs >= obsCostGeode and (oreCostObs <= time or clayCostObs <= time)):
    a = recurse(bp,oreRob,clayRob, obsRob,geodeRobot+1, ore-oreCostGeode + oreRob, clay + clayRob,obs - obsCostGeode+ obsRob,geodes + geodeRobot, time-1)
    if(a > maxGeodes):
      maxGeodes = a
  if(ore >=oreCostObs and clay >=  clayCostObs and (oreCostGeode <= time or obsCostGeode <= time)):
    a = recurse(bp,oreRob,clayRob, obsRob+1,geodeRobot, ore-oreCostObs + oreRob, clay-clayCostObs + clayRob,obs + obsRob,geodes + geodeRobot, time-1)
    if(a > maxGeodes):
      maxGeodes = a
  DP[c] = maxGeodes
  return maxGeodes

DP = {}
# print(recurse(blueprints[0]))
print(recurse(blueprints[1]))

# totalScore = 1
# for bp in blueprints[:3]:
#   DP = {}
#   holder = recurse(bp)
#   totalScore *= holder
#   print(holder)

# print(totalScore)

# 1 : 9, 2: 23, 3:11
  
  
  