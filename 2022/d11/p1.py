from math import floor

f = open("sample.txt", "r")

inp = f.read()
parsed = inp.split("\n")

class Monkey:
  def __init__(self,id, items, operation, test, ifTrue, ifFalse):
    self.id = id
    self.items = items
    self.operation = operation
    self.test = test
    self.ifTrue = ifTrue
    self.ifFalse = ifFalse
    self.totalInspected = 0
  def print(self):
    print("ID : {}, items : {}, operation : {}, test : {}, ifTrue : {}, ifFalse {}".format(self.id,self.items,self.operation,self.test,self.ifTrue, self.ifFalse))
monkeys = {}

for i in range(0,len(parsed),7):
  monkeyId= i//7 # Monkey identifier
  startingItems = list(map(int,parsed[i+1].replace(",", "").split(" ")[4:])) # The items that the monkey starts with FORM : [Int]
  operation = " ".join(parsed[i+2].split(" ")[5:]) # What to do with the stress level FORM : "[operator] [operand]"
  test = int(parsed[i+3].split(" ")[-1]) # How to tell if you should throw current item (what to be divisble by) FORM : Int
  trueAction = int(parsed[i+4].split(" ")[-1]) # Who to throw to if test passes FORM : Int
  falseAction = int(parsed[i+5].split(" ")[-1]) # Who to throw to if test fails FORM : Int
  
  monkeys[monkeyId] = Monkey(monkeyId, startingItems, operation, test, trueAction, falseAction)

def elapseRound(monkeys):
  for _,monkey in monkeys.items():
    for _,item in enumerate(monkey.items):
      old = item
      new = eval(monkey.operation)
      newDiv3 = floor(new/3)
      if(newDiv3 % monkey.test == 0):
        monkeys[monkey.ifTrue].items.append(newDiv3)
      else:
        monkeys[monkey.ifFalse].items.append(newDiv3)
    monkey.totalInspected = monkey.totalInspected + len(monkey.items)
    monkey.items = []

for i in range(20):
  elapseRound(monkeys)

totalInspectedArray = sorted([(monkey.totalInspected) for (_,monkey) in monkeys.items()])
monkeyBusiness = totalInspectedArray[-1] * totalInspectedArray[-2]
print(monkeyBusiness)