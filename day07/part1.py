import polars
from enum import Enum
import bisect

base = 13
minimum = 7

cardValues = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 11,
    "T": 10,
    **{str(i): i for i in range(10)}
}
def getHandValue(first, second):
    if first == 5:
        return 6 
    elif first == 4:
        return 5
    elif first == 3 and second == 2:
        return 4
    elif first == 3 and second < 2:
        return 3
    elif first == 2 and second == 2:
        return 2
    elif first == 2 and second == 1:
        return 1
    else:
        return 0

def computeValue(string):
    value = 0
    i = 5
    for c in string:
        value += cardValues[c] * (base**i)
        i -= 1
    print(string)
    acc = polars.DataFrame(string).group_by(by="column_0").count().sort(by="count", descending=True)
    if(len(acc) == 1):
        first = 5
        second = 0
    else:
        first, second = acc["count"][0:2] 
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
print(hands)
print(bids)
print()

solution = []
for i in range(len(hands)):
    h = hands[i]
    b = bids[i]
    value = computeValue(h)
    bisect.insort(solution, (value, int(b)))
print(solution)
    
L = len(solution)
res = 0
for i in range(L):
    print(f"{i+1} * {solution[i][1]}")
    res += (i+1) * solution[i][1]
print(res)