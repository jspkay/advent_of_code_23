
"""
times = [7, 15, 30]
distances = [9, 40, 200] # """

"""
times = [47, 98, 66, 98]
distances = [400, 1213, 1011, 1540] # """

def getNumberOfWays(t, d):
    res = 0
    for speed in range(t+1):
        remainingTime = t-speed
        totalDistanceTravelled = speed * remainingTime
        if(totalDistanceTravelled > d):
            res += 1
            """ print(f"Good combination: hold the button for {speed}, you'd reach {totalDistanceTravelled}")
        else:
            print(f"pushing it for {speed} would not get you there - {totalDistanceTravelled}")"""
    return res
    
times = [47986698]
distances = [400121310111540]

solution = 1
for i in range(len(times)):
    solution *= getNumberOfWays(times[i], distances[i])
    print("------")
print(f"Solution is {solution}")