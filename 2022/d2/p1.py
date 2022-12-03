f = open("input.txt", "r")
inp = f.read()

a = [x.split() for x in inp.split('\n')]

elfPlays = []
youPlays = []

score = 0
scores = {"X" : 1, "Y" : 2, "Z" : 3}
same = {"X":"A", "Y" : "B", "Z" : "C"}
for i in a:
  e = i[0]
  y = i[1]
  score += scores[y]
  if(same[y] == e):
    score +=3 # Draw
  elif( (e == "A" and y == "Y") or (e == "B" and y == "Z") or (e == "C" and y == "X") ):
    score+=6 # Win
  # Do nothing for loss
    
print(score)

  
  



