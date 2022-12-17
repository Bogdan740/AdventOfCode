from json import loads 
from functools import cmp_to_key
f = open("input.txt", "r")

inp = f.read().split("\n")

packets = []

for i in range(0,len(inp),3):
  packets += [loads(inp[i]),loads(inp[i+1])]


def compare(l,r):
  lISint = (type(l) == int)
  rISint = (type(r) == int)
  # If both l and r and integers
  if(lISint and rISint):
    return l - r # NEGATIVE : means right order, POSITIVE : Means wrong order, 0 : indeterminate
  # If both l and r are lists
  elif(not lISint and not rISint):
    pointer = 0
    while(pointer < len(l) and pointer < len(r)):
      # print("TING",l[pointer],r[pointer])
      diff = compare(l[pointer],r[pointer])
      pointer+=1
      if(diff == 0):
        continue
      else:
        return diff #  NEGATIVE : means right order, POSITIVE : Means wrong order
    return len(l) - len(r) #  NEGATIVE : means right order, POSITIVE : Means wrong order, 0 : Indeterminate
  elif(lISint and not rISint):
    return compare([l],r)
  elif(not lISint and rISint):
    return compare(l,[r])

counter2 = 0
counter6 = 0
for i in packets:
  counter2 += (compare(i,[2]) < 0)
counter6 = 0
for i in packets + [2]:
  counter6 += (compare(i,[6]) < 0)

print((counter2 + 1) * (counter6 + 1))
  