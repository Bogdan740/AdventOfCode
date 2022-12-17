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

packets = packets + [[2],[6]]
sorted_packets = sorted(packets, key=cmp_to_key(compare))
index_div_1 = sorted_packets.index([2]) + 1
index_div_2 = sorted_packets.index([6]) + 1
print(index_div_1 * index_div_2)