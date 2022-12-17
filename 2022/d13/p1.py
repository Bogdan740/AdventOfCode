from json import loads 
f = open("input.txt", "r")

inp = f.read().split("\n")

pairs = []

for i in range(0,len(inp),3):
  a = inp[i]
  b = inp[i+1]
  pairs.append( (loads(a),loads(b)) )


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
    
  
correct = 0

for i,(x,y) in enumerate(pairs):
  correct += (compare(x,y) < 0) * (i+1)

print(correct)
  