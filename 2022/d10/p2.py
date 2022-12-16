from math import sqrt

f = open("input.txt", "r")

inp = f.read()
parsed = [i.split(" ") for i in inp.split("\n")]

screen = ['K' for _ in range(240)]

def draw(cycle,x,screen):
  screen[cycle-1] = '#' if x-1 <= (cycle -1)%40  <= x+1 else '.'
x = 1
cycle = 0
for cmd in parsed:
  if(cmd[0] == "noop"):
    cycle +=1
    draw(cycle,x,screen)
  else:
    for _ in range(2):
      cycle +=1
      draw(cycle,x,screen)
    x+=int(cmd[1])

    
for i in range(0,len(screen),40):
  print("".join(screen[i:i+40]))
      
    
