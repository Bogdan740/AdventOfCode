f = open("input.txt", "r")
monkeys= [line.split(": ")for line in f.read().split("\n")]

for i,(name,op) in enumerate(monkeys):
  try:
    monkeys[i] = (name,int(op))
  except ValueError:
    monkeys[i] = (name, [op[0:4],op[-4:]],eval('lambda x,y:x{}y'.format(op[5])))
    pass
monkeys = {i[0]:(i[1:]) for i in monkeys}

def recurse(monkeyName):
  val,*func = monkeys[monkeyName]
  if(type(val) == int):
    return val
  else:
    return func[0](recurse(val[0]),recurse(val[1]))

print(int(recurse("root")))
  


  