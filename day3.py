import os

def chunkstring(string, length):
    return (string[0+i:length+i] for i in range(0, len(string), length))    

def get_value(s):
    r = 0
    if s.isupper():
        return ord(s) - ord("A") + 27       
    else:
        return ord(s) - ord("a") + 1

def to_value_list( input):
    result = []
    parts = list(input)
    for i in parts:
        result.append(get_value(i))
    return result

class Rucksack:
    def __init__(self, contents) -> None:
        size = len(contents) // 2 # // to int - / to float
        chunks = chunkstring(contents, size)
        self.content = contents
        self.c1 = contents[0:size]
        self.c2 = contents[size:len(contents)]

    def find_duplicate(self):
        for i in self.c1:
            if i in self.c2:
                return get_value(i)
        return 0

class RucksackGroup:
    def __init__(self, r1, r2, r3) -> None:
        self.r1 = r1
        self.r2 = r2
        self.r3 = r3

    def get_priority(self):
        for i in self.r1.content:
            if i in self.r2.content and i in self.r3.content:
                return get_value(i)
        return 0

rucksacks = []

directory = os.path.dirname(os.path.abspath(__file__))
with open(directory + "\\data\\day3.txt") as f:
   for line in f:
    rucksacks.append( Rucksack(line[0:len(line)-1])) # strip linebreak

#print (rucksacks[0].find_duplicate())

sum = 0
for i in rucksacks:
    sum += i.find_duplicate()    

print(sum) # 7446

groups = []
for i in range(0, len(rucksacks), 3):
    groups.append(RucksackGroup(rucksacks[i],rucksacks[i+1],rucksacks[i+2]))

sum_group = 0
for i in groups:
    sum_group += i.get_priority()    

print(sum_group) # 2646
