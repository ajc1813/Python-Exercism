#def best_hands(hands):
    #pass

from collections import Counter
card2num = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14
}
def preprocess(hand):
    cards = sorted([(card2num[x[:-1]], x[-1]) for x in hand.split()], key=lambda x: x[0])
    if (
        cards[-1][0] == 14 and
        not sequential(cards)
    ):
        low_ace = [(1,cards[-1][1])] + cards[:-1]
        if all([(x[0]-y[0])==1 for x,y in zip(low_ace[1:], low_ace[:-1])]):
            return low_ace
    return cards
def samesuite(hand):
    suite = hand[0][1]
    return all([x[1]==suite for x in hand[1:]])
def sequential(hand):
    return all([(x[0]-y[0])==1 for x,y in zip(hand[1:], hand[:-1])])
def straightflush(hand):
    return samesuite(hand) and sequential(hand)
def get_high_hand(candidates):
    winners = []
    high = []
    for cand in candidates:
        if cand[3] > high:
            high = cand[3]
    for cand in candidates:
        if cand[3] == high:
            winners.append(cand[0])
    return winners
    
def get_high_2pair(candidates, kind):
    high = 0
    new_cands = []
    for cand in candidates:
        h = max([k for k,v in cand[2].items() if v==kind])
        if h > high:
            high = h
    for cand in candidates:
        h = max([k for k,v in cand[2].items() if v==kind])
        if h == high:
            new_cands.append(cand)
    if len(new_cands) == 1:
        return [new_cands[0][0]]
    else:
        return get_high_pair([
            [cand[0], cand[1], 
            {k:v for k,v in cand[2].items() if k != h}, 
            [x for x in cand[3] if x != h],
            cand[4]]for cand in new_cands
        ], 2)
def get_high_pair(candidates, kind):
    high = 0
    new_cands = []
    for cand in candidates:
        h = [k for k,v in cand[2].items() if v==kind][0]
        if h > high:
            high = h
    for cand in candidates:
        h = [k for k,v in cand[2].items() if v==kind][0]
        if h == high:
            new_cands.append(cand)
    if len(new_cands) == 1:
        return [new_cands[0][0]]
    else:
        return get_high_hand([[cand[0], cand[1], cand[2], [x for x in cand[3] if x != h], cand[4]]for cand in new_cands])
def best_hands(hands):
    hand_score = []
    for hand in hands:
        cards = preprocess(hand)
        numbers = sorted([x[0] for x in cards])
        kind_counts = Counter(numbers)
        if straightflush(cards):
            hand_score.append((hand, cards, kind_counts, numbers, 9))
        elif 4 in kind_counts.values():
            hand_score.append((hand, cards, kind_counts, numbers, 8))
        elif (3 in kind_counts.values()) and (2 in kind_counts.values()):
            hand_score.append((hand, cards, kind_counts, numbers, 7))
        elif samesuite(cards):
            hand_score.append((hand, cards, kind_counts, numbers, 6))
        elif sequential(cards):
            hand_score.append((hand, cards, kind_counts, numbers, 5))
        elif 3 in kind_counts.values():
            hand_score.append((hand, cards, kind_counts, numbers, 4))
        elif sum([1 for x in kind_counts.values() if x==2])==2:
            hand_score.append((hand, cards, kind_counts, numbers, 3))
        elif 2 in kind_counts.values():
            hand_score.append((hand, cards, kind_counts, numbers, 2))
        else:
            hand_score.append((hand, cards, kind_counts, numbers, 1))
    hand_score.sort(key=lambda x: x[-1])
    high_score = hand_score[-1][-1]
    candidates = [x for x in hand_score if x[-1]==high_score]
    if len(candidates) == 1:
        return [candidates[0][0]]
    winners = []
    if high_score == 1:
        winners += get_high_hand(candidates)
    elif high_score == 2:
        winners += get_high_pair(candidates, 2)
    elif high_score == 3:
        winners += get_high_2pair(candidates, 2)
    elif high_score == 4:
        winners += get_high_pair(candidates, 3)
    elif high_score == 5:
        winners += get_high_hand(candidates)
    elif high_score == 6:
        winners += get_high_hand(candidates)
    elif high_score == 7:
        winners += get_high_2pair(candidates, 3)
    elif high_score == 8:
        winners += get_high_pair(candidates, 4)
    elif high_score == 9:
        winners += get_high_hand(candidates)
    return winners
            #last=[character for character in element[1:][::3]]
            #last_element+=[last]
            #if len(set(first_element))==1:
                #rank.append(10)
            #elif (sorted(first_element) == list(range(min(first_element), max(first_element)+1))) and len(set(last_element))==1:
                #rank.append(9)
            #return rank
                