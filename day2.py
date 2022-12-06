import os

# 1 for Rock, 2 for Paper, and 3 for Scissors
mapper = {'A':1, 'B': 2, 'C': 3, 'X':1, 'Y': 2, 'Z': 3, }

def to_int( val ):
   return mapper.get(val,-1)

def win():
    return 6

def draw():
    return 3

def lose():
    return 0

def rock_paper_scissor(p1, p2):
    if p1 == p2:
        return draw()
    elif p1 == 1 and p2 == 3: # rock beats scissor
        return win()
    elif p1 == 2 and p2 == 1: # paper beats rock
        return win()
    elif p1 == 3 and p2 == 2: # scissor beats paper
        return win()
    else:
        return lose()

def get_win( input):
    if input == 3:
        return 1
    else:
        return input + 1

def get_lose( input):
    if input == 1:
        return 3
    else:
        return input - 1

def change_input(input,  conclusion):
    if conclusion == 2: # draw
        return input
    elif conclusion == 3: # win
        return get_win(input)      
    else: # lose
       return get_lose(input)

def get_result_p1(opponent, me):
    my_val = to_int(me)
    opp_val = to_int(opponent)
    return rock_paper_scissor(my_val, opp_val) + my_val;

def get_result_p2(opponent, me):
    my_val = to_int(me)
    opp_val = to_int(opponent)
    my_val = change_input(opp_val, my_val)
    return rock_paper_scissor(my_val, opp_val) + my_val;

score_p1 = 0
score_p2 = 0

directory = os.path.dirname(os.path.abspath(__file__))
with open(directory + "\\data\\day2.txt") as f:
   for line in f:
    split = line.split()
    score_p1 += get_result_p1(split[0], split[1])
    score_p2 += get_result_p2(split[0], split[1])

print(score_p1) # 10624
print(score_p2) # 14060



   


