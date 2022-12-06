import os

# Day 1 Calorie Counting - https://adventofcode.com/2022/day/1

calories_by_elf = {}
id = 0
directory = os.path.dirname(os.path.abspath(__file__))
with open(directory + "\\data\\day1.txt") as f:
   for line in f:
    if '\n' == line:
        id+=1
    else:
        calories_by_elf[id] = calories_by_elf.get(id,0) + int(line)

print(calories_by_elf)

max = 0
for key, value in calories_by_elf.items():
    if value > max:
        max = value
        id = key

print(max) # 69626

# part 2

sorted = sorted(calories_by_elf.items(), key=lambda item: item[1],reverse=True)
# print(sorted)

sum = 0 
top_N_Elves = 3
for i in range(0, top_N_Elves):
    sum += sorted[i][1]

print(sum) # 206780