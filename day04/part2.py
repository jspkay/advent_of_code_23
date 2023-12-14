import enum
import sys

"""
STRATEGIA CORRETTA:
    1. Generare una mappa diretta tra seme e location
    2. Con questa mappa si hanno i range dei semi
    3. Per ogni coppia di semi in ingresso (start, length) si controlla a quali valori vengono mappati
    4. Si determina il minimo >Z
"""                         


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
seeds = []
for line in contents:
    if line == "":
        continue
    if line[0].isalpha():
        first_word = line.replace(":", "").split(" ")[0]
        if first_word == "seeds":
            print(line)
            seeds_str = line.split(" ")[1:]
            for i in range(len(seeds_str)//2):
                x = i*2
                print(seeds_str[x], " ", seeds_str[x+1])
                seeds.append( (int(seeds_str[x]), int(seeds_str[x+1])) )
            print(seeds)
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
import sys
solution = sys.float_info.max
for seed in seeds:
    for value in range(seed[0], seed[0]+seed[1]):
        current_value = value
        for i in range(1, len(maps)):
            current_value = maps[i].map(current_value)
        print(current_value)
        if current_value < solution:
            solution = current_value
print("solution is: ", solution)
    


        
        