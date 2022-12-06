#! usr/bin/python3 
from collections import Counter

packets = []
with open("day6in.txt", 'r') as file:
    for line in file:
        for i in range(len(line.rstrip())):
            packets.append(line[i])
            if packets.count(line[i]) > 1:
                packets = packets[packets.index(line[i])+1:]
            
            # len packets == 4 for part 1 
            if len(packets) == 14 and max(Counter(packets).values()) == 1:
                print(i+1)
                packets.clear()
                break

