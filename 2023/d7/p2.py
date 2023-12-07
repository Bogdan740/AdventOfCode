lines = None
with open("input.txt", "r") as fp:
    lines = fp.read().split("\n")

# lines=["22333 765"]


parsed = [(line.split()[0],int(line.split()[1])) for line in lines]
strength =  {i:13-j for j,i in enumerate("AKQT98765432J")}

hand_bid_type = []
for hand,bid in parsed:
    num_j = hand.count("J")

    is_full_house = False
    is_two_pair = False
    hand_no_J = hand.replace("J","")
    
    for i in hand_no_J:
        num_j_left = num_j
        count_i = hand_no_J.count(i)
        if(count_i + num_j_left < 3):
            continue
        num_j_left-=(3-count_i)
        num_j_left = 0 if num_j_left < 0 else num_j_left
        for j in hand_no_J:
            if(i == j):
                continue
            count_j = hand_no_J.count(j)
            if(count_j == 2-num_j_left or num_j_left == 2):
                is_full_house = True
                
    for i in hand_no_J:
        num_j_left = num_j
        count_i = hand_no_J.count(i)
        if(count_i + num_j_left < 2):
            continue
        num_j_left-=(2-count_i)
        num_j_left = 0 if num_j_left < 0 else num_j_left
        for j in hand_no_J:
            if(i == j):
                continue
            count_j = hand_no_J.count(j)
            if(count_j == 2-num_j_left or num_j_left == 2):
                is_two_pair = True
                
    if(any(hand_no_J.count(i) == 5 - num_j for i in hand_no_J if i!="J") or num_j == 5): # Five of a kind
        hand_bid_type.append((hand,bid,7))
        
    elif(any(hand_no_J.count(i) == 4 - num_j for i in hand_no_J if i!="J") or num_j == 4): # Four of a kind
        hand_bid_type.append((hand,bid,6))
        
    elif(is_full_house): # Full house
        hand_bid_type.append((hand,bid,5))
        
    elif(any(hand_no_J.count(i) == 3-num_j for i in hand_no_J if i!="J") or num_j == 3): # 3 of a kind
        hand_bid_type.append((hand,bid,4))
        
    elif(is_two_pair): # Two pair - DO
        hand_bid_type.append((hand,bid,3))
        
    elif(any(hand_no_J.count(i) == 2-num_j for i in hand_no_J if i!="J") or num_j == 2):# One pair
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
