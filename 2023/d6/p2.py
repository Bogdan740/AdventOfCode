from math import floor,ceil

lines = None
with open("input.txt", "r") as fp:
    lines = fp.read().split("\n")

time = int(lines[0][11:].replace(" ",""))
distance = int(lines[1][11:].replace(" ",""))


dx=1e-5
r1 = ceil( ((-time + (time**2 - 4*distance)**0.5) / (-2)) + dx)
r2 = floor( ((-time - (time**2 - 4*distance)**0.5) / (-2)) - dx)
num_ways=r2-r1+1

print(num_ways)