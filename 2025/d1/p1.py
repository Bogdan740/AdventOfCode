with open("input.txt", "r") as f:
    input = f.readlines()

dial = 50
num_zeroes = 0
for line in input:
    dir = line[0]
    turn = int(line[1:])
    dial = (dial + (-1 if dir == "L" else 1) * turn) % 100
    if dial == 0:
        num_zeroes += 1

print(num_zeroes)
