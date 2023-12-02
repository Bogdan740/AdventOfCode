lines = None
with open("input.txt") as fp:
    lines = fp.read().split("\n")

parsed = [ [ [ (int(x.split()[0]),x.split()[1]) for x in k[1:].split(", ")] for k in line.split(":")[1].split(";")] for line in lines]

game_config = {
    "red" : 12,
    "green" : 13,
    "blue" : 14
}

possible_games = 0

for i,game in enumerate(parsed):
    is_possible = True
    for reveal in game:
        for num,col in reveal:
            if(num > game_config[col]):
                is_possible = False
            
    if(is_possible):
        possible_games+=i+1

print(possible_games)