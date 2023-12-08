lines = None
with open("test.txt", "r") as fp:
    lines=fp.read()

num_players, max_marble = (int(lines.split()[0]),int(lines.split()[-2]))
print(num_players, max_marble)

player = 1
score = {}

current = 0
circle = [0]

scores = {}
for i in range(1,max_marble+1):
    # print(f"CURRENT : {circle[current]}")
    # print(["_" + str(k) + "_" if k == circle[current] else k for k in circle])
    first_cw = (current+1) % len(circle)
    sec_cw = (current+2) % len(circle)
    if(i % 23 == 0):
        is_mult = True
        if(player not in scores):
            scores[player] = 0
            
        scores[player]+=i
        scores[player]+=circle[current-7]
        circle = circle[:current-7] + circle[current-7+1:]
        current = (current-7)%len(circle)
        player=(player+1)%num_players
        continue

    circle=circle[:first_cw+1] + [i] + circle[first_cw+1:]
    current = (first_cw+1)%len(circle)
    
    player=(player+1)%num_players

print(max(scores.values()))