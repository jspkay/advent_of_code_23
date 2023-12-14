import enum

f = open("input", "r")
contents = f.read().splitlines()

#               0        1          2           3        4           5           6            7
chain_list = ["seed", "soil", "fertilizer", "water", "light", "temperature", "humidity", "location"]
Properties = enum.Enum("property", chain_list, start=0)

class Map:
    def __init__(self, name):
        self.name = name
        self.start = []
        self.end = []
        self.difference = []
    def add_mapping(self, start, end, difference):
        self.start.append(start)
        self.end.append(end)
        self.difference.append(difference)
    
    def map(self, number):
        for i in range(len(self.start)):
            if self.start[i] <= number <= self.end[i]:
                return number + self.difference[i]
        return number
    
    def __repr__(self):
        res = f"map {self.name}\n----------------------\n"
        res += "start\tend\tdifference\n"
        for i in range(101):
            res += f"{i} -> {self.map(i)}\n"
        #for i in range(len(self.start)):
        #    res += f"{self.start[i]}\t{self.end[i]}\t{self.difference[i]}\n"
        return res

state = Properties.seed
maps = [Map(name="seeds")]
for line in contents:
    if line == "":
        continue
    if line[0].isalpha():
        first_word = line.replace(":", "").split(" ")[0]
        if first_word == "seeds":
            print(line)
            seeds = line.split(" ")[1:]
            print(seeds)
            seeds = [int(i) for i in seeds]
            continue
        else:
            for i in range(len(chain_list)-1):
                if first_word == chain_list[i] + "-to-" + chain_list[i+1]:
                    print("Mapping: ", first_word, " ", chain_list[i] + "-to-" + chain_list[i+1])
                    state = Properties[chain_list[i+1]]
                    maps.append(Map(name = state.name))
                    continue
    else:
        destination, source, length = line.split(" ")
        
        m = maps[ state.value ]
        
        difference = int(destination) - int(source)
        start = int(source)
        end = int(source) + int(length)
        
        m.add_mapping(start, end, difference)
        
print(seeds)
locations = []
for seed in seeds:
    current_value = seed
    for i in range(1, len(maps)):
        current_value = maps[i].map(current_value)
    print(current_value)
    locations.append(current_value)

print(locations)
print("solution is: ", min(locations))
    


        
        