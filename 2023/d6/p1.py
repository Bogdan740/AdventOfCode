from math import floor,ceil

lines = None
with open("input.txt", "r") as fp:
    lines = fp.read().split("\n")

times = [int(i) for i in lines[0][11:].replace("  ", " ").split()]
distances = [int(i) for i in lines[1][11:].replace("  ", " ").split()]
races = zip(times,distances)

num_ways = 1
dx=1e-10
for race_time,best_dist in races:
    r1 = ceil( ((-race_time + (race_time**2 - 4*best_dist)**0.5) / (-2)) + dx)
    r2 = floor( ((-race_time - (race_time**2 - 4*best_dist)**0.5) / (-2)) - dx)
    num_ways*=r2-r1+1

print(num_ways)