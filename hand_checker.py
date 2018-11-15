from collections import defaultdict

card_order_d = ["2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":11, "Q":12, "K":13, "A":14]

def check_hand(h1,h2):
    #This function checks the hands for the winner


def check_straight_flush(H):
    if check_flush(H) and check_straight(H):
        return True
    else:
        return False

def check_four_kind(H):
    values = [i[0] for i in H]
    value_c = defaultdict(lambda:0)
    for v in values:
        value_c[v]+=1
    if sorted(value_c.values()) == [1,4]:
        return True
    return False

def check_full_house(H):
    values = [i[0] for i in H]
    value_c = defaultdict(lambda:0)
    for v in values:
        value_c[v]+=1
    if sorted(value_c.values()) == [2,3]:
        return True
    return False


def check_flush(H):
    suits = [i[1] for i in H]
    if len(set(suits))==1:
        return True
    return False

def check_straight(H):
    values = [i[0] for i in H]
    value_c = defaultdict(lambda:0)
    for v in values:
        value_c[v]+=1
    rank_v = [card_order_d[i] for i in values]
    value_r = max(rank_v) - min(rank_v)

    if len(set(value_c.values())) == 1 and (value_r==4):
        return True
    else:
        if set(values)== set(["A","2","3","4","5"]):
            return True
        return False

