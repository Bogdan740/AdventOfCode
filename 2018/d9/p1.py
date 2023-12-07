lines = None
with open("test.txt", "r") as fp:
    lines=fp.read()

num_players, max_marble = (int(lines.split()[0]),int(lines.split()[-2]))

player = 1
score = {}

last = 0
circle = [0]

scores = {}
for i in range(1,max_marble+1):
    first_cw = (last+1) % len(circle)
    sec_cw = (last+2) % len(circle)
    if(i % 23 == 0):
        if(player not in scores):
            scores[player] = 0
            
        scores[player]+=i
        scores[player]+=circle[last-7]
        circle = circle[:last-7] + circle[last-7+1:]
        last = last-7
        if(last==-1):
            last=0
        continue
        
    circle=circle[:first_cw+1] + [i] + circle[first_cw+1:]
    last = first_cw+1
    
    player+=1
        
print(max(scores.values()))