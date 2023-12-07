lines = None
with open("input.txt", "r") as fp:
    lines = fp.read().split("\n")

parsed = [(line.split()[0],int(line.split()[1])) for line in lines]
strength =  {i:13-j for j,i in enumerate("AKQJT98765432")}

hand_bid_type = []
for hand,bid in parsed:
    if(all(i==hand[0] for i in hand)): # Five of a kind
        hand_bid_type.append((hand,bid,7))
        
    elif(any(hand.count(i) == 4 for i in hand for j in hand)): # Four of a kind
        hand_bid_type.append((hand,bid,6))
        
    elif(any(hand.count(i) == 3 and hand.count(j) == 2 for i in hand for j in hand)): # Full house - DO
        hand_bid_type.append((hand,bid,5))
        
    elif(any(hand.count(i) == 3 for i in hand)): # 3 of a kind
        hand_bid_type.append((hand,bid,4))
        
    elif(any(hand.count(i) == 2 and hand.count(j) == 2 and i != j for i in hand for j in hand)): # Two pair - DO
        hand_bid_type.append((hand,bid,3))
        
    elif(any(hand.count(i) == 2 for i in hand)):# One pair
        hand_bid_type.append((hand,bid,2))
        
    else: # High card
        hand_bid_type.append((hand,bid,1))
    

hand_bid_type_score = []
for hand,bid,typ in hand_bid_type:
    score = 0
    for i,card in enumerate(hand):
        score += strength[card]*(10**(2*(5-i)))
    hand_bid_type_score.append((hand,bid,typ,score))

card_bids_sorted = [x[1] for x in sorted(hand_bid_type_score, key=lambda x:(x[2],x[3]))]
total_winnings = sum(x*(i+1) for i,x in enumerate(card_bids_sorted))
print(total_winnings)
