import os

class File:
    def __init__(self, size, name) -> None:
        self.name = name
        self.size = int(size)

    def get_size(self):
        return self.size

class Directory:
    def __init__(self, name, parent) -> None:
        self.name = name
        self.parent = parent
        self.items = []

    def add(self, item):
        self.items.append(item)
    
    def get_size(self):
        total = 0
        for i in self.items:
            total += i.get_size()

        return total

def add_directory(name):
    path = active[0] + '/' + name    
    dir = Directory(path, flat_list.get(active[0]))
    flat_list[path] = dir
    current = flat_list.get(active[0])
    current.add(dir)

def change_directory(dir):
    if dir == '/':       
        active[0] = '/'
    elif dir == '..':
        item = flat_list.get(active[0])
        active[0] = item.parent.name
    else:
        active[0] = active[0] + '/' +dir

def parse_command(command):
    if command[0] == "$":
        if command[2:4] == "ls":
            pass
        elif command[2:4] == "cd":
            split = command.split(" ")
            change_directory(split[-1])

    elif command[0:3] == "dir": 
        add_directory(command[4:])

    else: # file
        sizeAndName = command.split()
        item = flat_list.get(active[0])
        item.add(File(sizeAndName[0], sizeAndName[1]))


flat_list = { '/': Directory('/', None) }
active = ['/']

diskspace = 70000000
required_space = 30000000

directory = os.path.dirname(os.path.abspath(__file__))
with open(directory + "\\data\\day7.txt") as f:
   for line in f:
    parse_command(line.rstrip())

max = 100000
sum = 0
for key, dir in flat_list.items():
    if key == '/':
        continue
    size = dir.get_size()
    if size <= max:
        print(key)
        sum += size

print(sum) # 1611443

# part 2

used_space = flat_list.get('/').get_size()
unused_space = diskspace - used_space
required = required_space - unused_space
candidate_size = diskspace;

def find_dir_to_delete( items, size):
    candidate_size = size
    for item in items:
        if type(item) == File:
            continue
        size = item.get_size()
        if size > required:
            if candidate_size > size:
                candidate_size = size                
    return candidate_size   

                
candidate = None
root = flat_list.get('/')


for key, dir in flat_list.items():
    candidate_size = find_dir_to_delete(dir.items, candidate_size)

print(candidate)
print(candidate_size) # 2086088
