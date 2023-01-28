import os

def sign(val: int) -> int:
    if val < 0:
        return -1
    elif val > 0:
        return 1
    else:
        return 0

class Position():
    def __init__(self, x=0, y=0) -> None:
        self.x = x
        self.y = y

    def sign(self) -> 'Position':
        x = sign(self.x)
        y = sign(self.y)
        return Position(x,y)

    def __add__(self, other: 'Position'):
        return Position(self.x + other.x, self.y + other.y)
    def __sub__(self, other: 'Position') :
        return Position(self.x - other.x, self.y - other.y)
    def __repr__(self) -> str:
        return "({0},{1})".format(self.x,self.y)

    def __hash__(self):
        return hash((self.x,self.y))
    def __eq__(self, other: 'Position') -> bool:
        return self.x == other.x and self.y == other.y

class Knot():
    def __init__(self, name: str) -> None:
        self.name = name
        self.position = Position()
        self.steps = 0
        self.history = []

    def __repr__(self) -> str:
        return "{0} - {1} - steps: {2}".format(self.name, self.position, self.steps)
    def move(self, pos : Position):
        self.history.append(self.position)
        self.position += pos
        self.steps += 1
        #print("{0} moved from {1} to {2}".format(self.name, self.history[-1], self.position))
           
    def follow(self, knot: 'Knot'):
        offset = knot.position - self.position

        if abs(offset.x) > 1 or abs(offset.y) > 1:
            self.move(offset.sign())

def get_movement(move: str): # -> List[Position]:
    dir, step = move.split()
    movement = []
    for i in range( 0, int(step)):
        if dir == 'L':        
            movement.append(Position(-1,0))
        elif dir == 'R':
            movement.append(Position(1,0))
        elif dir == 'U':
            movement.append(Position(0,1))
        elif dir == 'D':
            movement.append(Position(0,-1)) 
    return movement

def parse_movement(move: str, head: Knot, tail: Knot):
    movement = get_movement(move)
    #print("===========")
    #print(move)
    #print( head)
    #print( tail)
    for step in movement:
        head.move(step)
        tail.follow(head)
    #print( head)
    #print( tail)

def parse_movement_p2(move: str, head: Knot, knots):
    movement = get_movement(move)
    #print("===========")
    #print(move)
    #print( head)
    #print( tail)

    active = None;
    for step in movement:
        head.move(step)
        active = head
        for k in knots:
            k.follow(active)
            active = k
            
    #print( head)
    #print( tail)

def part_1():
    head_ = Knot('H')
    tail_ = Knot('T')

    directory = os.path.dirname(os.path.abspath(__file__))
    with open(directory + "\\data\\day9.txt") as f:
        for line in f:
            parse_movement(line.rstrip(), head_, tail_)

    print( head_)
    print( tail_)

    s = set(tail_.history)
    print(len(s)+1) #+1 compensate for start pos


def part_2():
    head_ = Knot('H')
    knots = []
    for i in range(9):
        knots.append(Knot(str(i+1)))

    directory = os.path.dirname(os.path.abspath(__file__))
    with open(directory + "\\data\\day9.txt") as f:
        for line in f:
            parse_movement_p2(line.rstrip(), head_, knots)

    print( head_)
    print( knots[8])

    s = set(knots[8].history)
    print(len(s)+1) #+1 compensate for start pos

#part_1()

part_2()