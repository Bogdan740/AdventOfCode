lines = None
with open("input.txt") as fp:
    lines = fp.read().split("\n")

parsed = [[int(line.split(": ")[0].split()[1])-1,[l1.split() for l1 in line.split(": ")[1].split(" | ")]] for line in lines]

cards = {card : 1 for card,_ in parsed}

for card,(got, win) in parsed:
    num_cards = cards[card]
    no_winning_nums = sum([1 if i in win else 0 for i in got])
    
    for i in range(card+1,card+1+no_winning_nums):
        cards[i]+=num_cards

print(sum(dict.values(cards)))
    