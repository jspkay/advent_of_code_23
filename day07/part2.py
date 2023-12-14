import polars
from enum import Enum
import bisect

"""
Wrong answers
248649845
"""

base = 13
minimum = 7

cardValues = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "T": 11,
    **{str(i): i for i in range(2,10)},
    "J": 1
}

def getHandValue(first, second):
    assert first+second <= 5, f"EHEH! YOU FOOL! first: {first} second: {second}"
    
    if first == 5:
        return 7 
    elif first == 4:
        return 6
    elif first == 3 and second == 2:
        return 5
    elif first == 3 and second < 2:
        return 4
    elif first == 2 and second == 2:
        return 3
    elif first == 2 and second == 1:
        return 2
    else:
        return 1

def computeValue(string):
    value = 0
    i = 5
    for c in string:
        value += cardValues[c] * (base**i)
        i -= 1
    df = polars.DataFrame(string).group_by(by="column_0").count().sort("count", descending=True)
    
    jokers_df = df.filter(df["column_0"] == "J")
    new_df = df.filter(df["column_0"] != "J")
    first_df = new_df[0]
    second_df = new_df[1]
    
    jokers = 0 if jokers_df.is_empty() else jokers_df["count"][0]
    first = 0 if first_df.is_empty() else first_df["count"][0]
    second = 0 if second_df.is_empty() else second_df["count"][0]
    
    # print(f"jokers {jokers}, first {first}, second {second}")
    
    first = first + jokers
        
    print(f"{string} -> {first}, {second}")
        
    value += getHandValue(first, second) * (base**7)
    
    return value

with open("input") as f:
    contents = f.read().splitlines()
    
hands = []
bids = []
for line in contents:
    h, b = line.split()
    hands.append(h)
    bids.append(b)

solution = []
for i in range(len(hands)):
    h = hands[i]
    b = bids[i]
    value = computeValue(h)
    bisect.insort_left(solution, (value, int(b), h))
    
print(solution)    

i = 1
for value in solution:
    print(f"{i} -> {value[2]}")
    i += 1

L = len(solution)
res = 0
for i in range(L):
    res += (i+1) * solution[i][1]
print(res)