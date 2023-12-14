f = open("input", "r")
contents = f.read().strip().split("\n")
f.close()

cards_duplicates = {}

solution = 0
for line in contents:
    card_id = int(line.replace("  ", " ").replace("  ", " ").split(":")[0].split(" ")[1])
    
    how_many_times = cards_duplicates.get(card_id, 0) + 1 # to get into account duplicates
    cards_duplicates.update({card_id: how_many_times})
    
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
    # tot = 2**(points-1) if points != 0 else 0
    
    for i in range(1, points+1):
        old = cards_duplicates.get(card_id+i, 0)
        cards_duplicates.update({card_id+i: old+how_many_times})
    
    print(cards_duplicates)
    
    total_cards = sum(cards_duplicates.values())
    print(total_cards)
print(total_cards)
