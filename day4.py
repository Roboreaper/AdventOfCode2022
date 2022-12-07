import os

def get_range(sectionsString):
    result = []
    list = sectionsString.split("-")
    start = int(list[0])
    end = int(list[1])+1
    for i in range(start, end):
        result.append(i)
    return result

class Assignment:
    def __init__(self, sectionsRaw) -> None:
        s = sectionsRaw.split(",")
        self.p1 = get_range(s[0])
        self.p2 = get_range(s[1])

    def contains(self) -> bool:
        x = all( item in self.p1 for item in self.p2) or all( item in self.p2 for item in self.p1)
        return x

    def overlap(self) -> bool:
        x = any( item in self.p1 for item in self.p2)
        return x

assignments = []
directory = os.path.dirname(os.path.abspath(__file__))
with open(directory + "\\data\\day4.txt") as f:
   for line in f:
    assignments.append( Assignment(line))

contain = 0
overlap = 0
for a in assignments:
    if a.contains():
        contain += 1
    if a.overlap():
        overlap += 1


print(contain) #477
print(overlap) #830
