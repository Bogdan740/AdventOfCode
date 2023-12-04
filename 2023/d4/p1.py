lines = None
with open("input.txt") as fp:
    lines = fp.read().split("\n")

parsed = [[l1.split() for l1 in line.split(": ")[1].split("|")] for line in lines]

points = 0

for got, win in parsed:
    no_winning_nums = sum([1 if i in win else 0 for i in got])
    points += 2**(no_winning_nums-1) if no_winning_nums != 0 else 0

print(points)