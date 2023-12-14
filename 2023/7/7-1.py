from collections import Counter
import functools


with open("inp.txt", "r") as f:
    hands = f.read().splitlines()


evaluatedHands = []

for hand in hands:
    cardsStr, bid = hand.split()
    cards = []
    for card in cardsStr:
        if card.isnumeric():
            cards.append(int(card))
        else:
            cards.append(list("TJQKA").index(card)+10)

    counts = Counter(cards)
    
    commons = counts.most_common()
    
    if commons[0][1] == 5: # five of a kind
        cards = [6] + cards
    elif commons[0][1] == 4: # Four of a kind
        cards = [5] + cards
    elif commons[0][1] == 3 and commons[1][1] == 2: # Full house
        cards = [4] + cards
    elif commons[0][1] == 3: # Three of a kind
        cards = [3] + cards
    elif commons[0][1] == 2 and commons[1][1] == 2: # Two pairs
        cards = [2] + cards
    elif commons[0][1] == 2: # One pair
        cards = [1] + cards
    else:
        cards = [0] + cards # High card
        
    cards += [int(bid)]
    
    evaluatedHands.append(cards)
    

def isBigger(a, b):
    for i in range(len(a)):
        if a[i] != b[i]:
            return 1 if a[i] > b[i] else -1
    
evaluatedHands.sort(key=functools.cmp_to_key(isBigger))

tot = 0

for i, cards in enumerate(evaluatedHands):
    tot += (i+1)*cards[-1]
    
print(tot)