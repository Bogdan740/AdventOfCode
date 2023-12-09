lines = None
with open("test.txt", "r") as fp:
    lines=fp.read()

num_players, max_marble = (int(lines.split()[0]),int(lines.split()[-2]))

player = 0
score = {}

current = 0
circle = [0]

scores = {}
for i in range(1,max_marble+1):
    # if(current == 0 or current == 1):
        # print(len(circle) ,circle)
    first_cw = (current+1) % len(circle)
    sec_cw = (current+2) % len(circle)
    if(i % 23 == 0):
        if(player not in scores):
            scores[player] = 0
        
        to_remove = (current-7)%len(circle)
            
        scores[player]+=i
        scores[player]+=circle[to_remove]
        circle.pop(to_remove)
        current = (to_remove)%len(circle)
        player=(player+1)%num_players
        continue
    

    circle=circle[:first_cw+1] + [i] + circle[first_cw+1:]
    current = (first_cw+1)%len(circle)
        
    
    player=(player+1)%num_players

print(max(scores.values()))