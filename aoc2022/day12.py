counter =0 
f = [l.rstrip() for l in open('day12.txt').readlines()]
for line in f:
    for char in line:
        if char.isdigit():
            counter += 1


print(counter)
