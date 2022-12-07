import os
from collections import deque

class Stack():
    def __init__(self) -> None:
        self.stack = deque()

    def add_box(self, box):
        if box != " ":
            self.stack.append(box)
        else:
            pass

    def pop_box(self):
        if len(self.stack) > 0:
            return self.stack.pop()

    def get_top_n(self, n):
        if len(self.stack) > 0:
            boxes = [None] * int(n)
            for i in reversed(range(int(n))):
                boxes[i] = self.stack.pop()
            return boxes


    def ontop(self):
        return self.stack[-1]


def move_9000(stacks, action):
    actions = action.split()
    move = actions[1]
    fr =  actions[3]
    to = actions[5]
    for i in range(0, int(move)):
        b = stacks[fr].pop_box()
        stacks[to].add_box(b)

def move_9001(stacks, action):
    actions = action.split()
    move = actions[1]
    fr =  actions[3]
    to = actions[5]
    boxes = stacks[fr].get_top_n(move)
    for b in boxes:       
        stacks[to].add_box(b)

# get each box and retain the spaces as empty places
def split_lines(line):
    n = 4
    return [line[i:i+n] for i in range(0, len(line), n)]

def create_stacks(raw, stacks):
    raw.reverse()
    ids = raw[0].split()
    for id in ids:
        stacks[id] = stacks.get(id , Stack())
    for item in raw[1:]:
      boxes = split_lines(item)
      for index, b in enumerate(boxes):
        y = b[1]
        id = str(index+1)
        stacks[id].add_box(y)

stacks = {}
init = True
rawLines = []
version = 9001

directory = os.path.dirname(os.path.abspath(__file__))
with open(directory + "\\data\\day5.txt") as f:
   for line in f:
    if init:
        if line in ['\n', '\r\n']:
            init = False
            create_stacks(rawLines,stacks)
        else:
            rawLines.append(line)
    else:
        if version is 9000:
            move_9000(stacks, line)
        else:
            move_9001(stacks, line)
    
top = ""
for i in stacks.items():
    top += i[1].ontop()

print (top) # -> JCMHLVGMG | LVMRWSSPZ


