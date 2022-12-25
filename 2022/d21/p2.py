f = open("input.txt", "r")
monkeys= [line.split(": ")for line in f.read().split("\n")]

for i,(name,op) in enumerate(monkeys):
  try:
    monkeys[i] = (name,int(op))
  except ValueError:
    monkeys[i] = (name, [op[0:4],op[-4:]],eval('lambda x,y:x{}y'.format(op[5])))
    pass
monkeys = {i[0]:(i[1:]) for i in monkeys}
monkeys["root"] = (monkeys["root"][0],lambda x,y : x == y)
monkeys["humn"] = (301,)

def recurse(monkeyName):
  if(monkeyName in DP):
    return DP[monkeyName]
  val,*func = monkeys[monkeyName]
  if(type(val) == int):
    DP[monkeyName] = val
    return val
  else:
    a,b = recurse(val[0]),recurse(val[1])
    if(monkeyName == "root"):
      return (func[0](a,b),a-b)
    toReturn = func[0](a,b)
    DP[monkeyName] = toReturn
    return toReturn

low,high = -10e15, 10e15

# We have to do binary search both assuming that "root" is an increasing and decreasing function as we don't know.
# One of the below while loops will not find anything. This coul be improved by checking if "root" is a decreasing or increasing
# function with respect to "humn" and do the appropriate loop
while(low < high):
  mid = (low + high) // 2
  monkeys["humn"] = (int(mid),)
  DP = {}
  check,diff = recurse("root")
  if(check):
    print(int(mid))
    break
  if(diff < 0):
    high = mid 
  else:
    low = mid

low,high = -10e15, 10e15

while(low < high):
  mid = (low + high) // 2
  monkeys["humn"] = (int(mid),)
  DP = {}
  check,diff = recurse("root")
  if(check):
    print(int(mid))
    break
  if(diff < 0):
    low = mid 
  else:
    high = mid
