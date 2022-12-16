from math import sqrt

f = open("input.txt", "r")

inp = f.read()
parsed = [i.split(" ") for i in inp.split("\n")]

x = 1
cycle = 0
signalStrength = 0
for cmd in parsed:
  if(cmd[0] == "noop"):
    cycle +=1
    if((cycle-20)%40 == 0 or cycle == 20):
      signalStrength += cycle*x
  else:
    num = int(cmd[1])
    cycle +=1
    if((cycle-20)%40 == 0 or cycle == 20):
      signalStrength += cycle*x
    cycle +=1
    if((cycle-20)%40 == 0 or cycle == 20):
      signalStrength += cycle*x
    x+=num
    
print(signalStrength)
      
    
