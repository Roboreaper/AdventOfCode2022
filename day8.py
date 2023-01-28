import os

def parse_row(line):
    row = []
    for c in line:
        row.append(int(c))
    return row

def get_height( forrest, x,y):
    return forrest[y][x]

def from_top(forrest, x,y ):
    val = get_height(forrest,x,y)

    for i in range (0, y):
        h = get_height(forrest, x, i)
        if h >= val:
            return False
    return True

def from_bottom(forrest, x,y ):
    val = get_height(forrest, x,y)

    r = range (y+1, len(forrest))
    for i in reversed(r):
        h = get_height(forrest, x, i)
        if h >= val:
            return False
    return True

def from_left(forrest, x,y ):
    val = get_height(forrest,x,y)

    for i in range(0, x):
        h = get_height( forrest, i, y)
        if h >= val:
            return False
    return True

def from_right(forrest, x,y ):
    val = get_height(forrest,x,y)

    r =range(x+1, len(forrest[0]))
    for i in reversed(r):
        h = get_height( forrest, i, y)
        if h >= val:
            return False
    return True

def is_visible( forrest, x, y):
    t = from_top(forrest, x, y)
    b = from_bottom(forrest, x, y)
    l = from_left(forrest, x, y)
    r = from_right(forrest, x, y)

    res = t or b or l or r
    return res


grid = []

directory = os.path.dirname(os.path.abspath(__file__))
with open(directory + "\\data\\day8.txt") as f:
   for line in f:
    grid.append( parse_row(line.rstrip()))

rows = len(grid)
columns = len(grid[0])

# dont count corners twice
visible = 2*rows +  2*columns - 4


# example test
# #print( visible )
# print( is_visible(grid, 1,2))

for x in range( 1, columns-1):
    for y in range ( 1, rows-1):
        if is_visible(grid, x,y):
            visible += 1

print( visible ) # 1818


# part 2

def look_up(forrest,x,y):
    val = get_height(forrest,x,y)
    up=0
    while(y != 0 ):
        y -= 1
        up+=1
        h = get_height(forrest,x,y)
        if h >= val:
            break
    return up

def look_down(forrest,x,y):
    val = get_height(forrest,x,y)
    down=0
    while(y != len(forrest[0])-1 ):
        y += 1
        down+=1
        h = get_height(forrest,x,y)
        if h >= val:
            break
    return down

def look_left(forrest,x,y):
    val = get_height(forrest,x,y)
    left = 0
    while(x != 0 ):
        x -= 1
        left+=1
        h = get_height(forrest,x,y)
        if h >= val:
            break
    return left

def look_right(forrest,x,y):
    val = get_height(forrest,x,y)
    right = 0
    while(x != len(forrest)-1 ):
        x += 1
        right+=1
        h = get_height(forrest,x,y)
        if h >= val:
            break
    return right

def scenic_score(forrest,x,y):
    val = get_height(forrest,x,y)
    
    return look_up(forrest,x,y) * look_down(forrest,x,y) *look_left(forrest,x,y) *look_right(forrest,x,y)
   

#print (scenic_score(grid, 2, 1))
#print (scenic_score(grid, 2, 3))

max = 0

for x in range( 1, columns-1):
    for y in range ( 1, rows-1):
        score = scenic_score(grid, x,y)
        if score > max:
            max = score
        
print ( max )  # 368368


    