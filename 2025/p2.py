with open("input.txt", "r") as f:
    input = f.readlines()

cur_dial = 50
num_zeroes = 0


def turn_dial(amount, dir):
    global cur_dial
    global num_zeroes

    if dir == "L":
        for _ in range(amount):
            cur_dial = (cur_dial - 1) % 100
            if cur_dial == 0:
                num_zeroes += 1
    else:
        for _ in range(amount):
            cur_dial = (cur_dial + 1) % 100
            if cur_dial == 0:
                num_zeroes += 1


for line in input:
    dir = line[0]
    turn = int(line[1:])

    turn_dial(turn, dir)

print(num_zeroes)
