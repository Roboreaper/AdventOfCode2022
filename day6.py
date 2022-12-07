import os

start_of_packet = 4
start_of_message = 14

def split_marker(marker, c):
    index = marker.find(c)
    return marker[index+1:len(marker)]

def update_marker(size, marker, c, start_of):
    if size >= start_of or c in marker:
        marker = split_marker( marker, c)
    return marker + c        

def find_start_message(data):
    marker = ""
    l = len(data)
    for index, c in enumerate(data):
        size = len(marker)
        if size == start_of_message: 
            return index       
        else:
            marker = update_marker(size, marker, c, start_of_message)
    return None

def find_start_marker(data):
    marker = ""
    l = len(data)
    for index, c in enumerate(data):
        size = len(marker)
        if size == start_of_packet:
            message_start = find_start_message(data)
            if message_start != None:
                return (index, message_start)
            else:
                marker = update_marker(size, marker, c, start_of_packet)
        else:
            marker = update_marker(size, marker, c, start_of_packet)

data = ""
directory = os.path.dirname(os.path.abspath(__file__))
with open(directory + "\\data\\day6.txt") as f:
    data = f.readline()

start = find_start_marker(data)

print (start) #1920|2334