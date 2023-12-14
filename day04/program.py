f = open("input", "r")
contents = f.read().strip().split("\n")
f.close()

solution = 0
for line in contents:
    numbers = line.split(":")[1]
    winning, mine = numbers.split("|")
    
    winning = [int(i) for i in list(filter(lambda x: x != '', winning.split(" ")))]
    mine = [int(i) for i in list(filter(lambda x: x != '', mine.strip().split(" ")))]
    
    print(winning)
    print(mine)
    
    points = 0
    for number in mine:
        if number in winning:
            points += 1
    tot = 2**(points-1) if points != 0 else 0 
    print(points, " -> ", tot)
    solution += tot
print(solution)
