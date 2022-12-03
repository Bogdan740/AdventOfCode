f = open("input.txt", "r")
inp = f.read()

a = [x.split() for x in inp.split('\n')]

elfPlays = []
youPlays = []

score = 0
draw = {"A": 1,"B" : 2, "C" : 3 }
win = {"A": 2,"B" : 3, "C" : 1 }
lose = {"A": 3,"B" : 1, "C" : 2 }
for i in a:
  e = i[0]
  y = i[1]
  if(y == "Z"): # WIN
    score+=6 + win[e]
  elif(y == "Y"): # Draw
    score+=3 + draw[e]
  else: #Lose
    score+=lose[e]
    
print(score)

  
  



