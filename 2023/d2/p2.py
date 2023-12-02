lines = None
with open("input.txt") as fp:
    lines = fp.read().split("\n")

parsed = [ [ [ (int(x.split()[0]),x.split()[1]) for x in k[1:].split(", ")] for k in line.split(":")[1].split(";")] for line in lines]

powers_sum = 0

for i,game in enumerate(parsed):
    d = {"red" : 0, "green" : 0, "blue" : 0}
    for reveal in game:
        for num,col in reveal:
            if(d[col] < num):
                d[col] = num
            
    powers_sum+=d["red"]*d["green"]*d["blue"]

print(powers_sum)