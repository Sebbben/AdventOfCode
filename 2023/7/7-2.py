from collections import Counter
import functools


with open("inp.txt", "r") as f:
    hands = f.read().splitlines()

# hands = """32T3K 765
# T55J5 684
# KK677 28
# KTJJT 220
# QQQJA 483""".splitlines()


evaluatedHands = []

for hand in hands:
    cardsStr, bid = hand.split()
    cards = []
    for card in cardsStr:
        if card.isnumeric():
            cards.append(int(card))
        elif card == "J":
            cards.append(0)
        else:
            cards.append(list("TQKA").index(card)+10)

    counts = Counter(cards)
    
    jokers = counts.get(0)
    if jokers is None: jokers = 0
    if 0 in counts: counts.pop(0)
    commons = counts.most_common()
    
    # print(counts.most_common(), jokers)
    if jokers == 5:# All joker = five of a kind
        cards = [6] + cards
    elif commons[0][1] + jokers == 5: # five of a kind
        cards = [6] + cards
    elif commons[0][1] + jokers == 4: # Four of a kind
        cards = [5] + cards
    elif commons[0][1] + jokers == 3 and commons[1][1] == 2: # Full house
        cards = [4] + cards
    elif commons[0][1] + jokers == 3: # Three of a kind
        cards = [3] + cards
    elif commons[0][1] == 2 and commons[1][1] + jokers == 2: # Two pairs
        cards = [2] + cards
    elif commons[0][1]+ jokers == 2: # One pair
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
# print(evaluatedHands)

tot = 0

for i, cards in enumerate(evaluatedHands):
    tot += (i+1)*cards[-1]
    
print(tot)