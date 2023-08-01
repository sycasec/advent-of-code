
def part1():
    cycles = 0
    X = 1
    file = open("day10.txt").readlines()
    markers = [220, 180, 140, 100, 60, 20]
    ss = []
    for line in file:
        if line[0] == 'a':
            cycles += 2
            if cycles >= markers[-1]:
                ss.append(markers.pop() * X)
            X += int(line[5:]) 
        elif line[0] == 'n':
            cycles += 1

        if len(markers) == 0:
            break

    print(sum(ss))

# part 2
X=1
file = [c.rstrip() for c in open("day10.txt").readlines()]
file.reverse()
crt = [['.' for i in range(40)] for j in range(6)] 
wait=0

def disp_crt():
    for l in crt: 
        print(*l, sep='')
    print('\n')

for i in range(6):
    for j in range(40):
        print(f"c={(i*40)+j}::op={file[-1]}::wait={wait}::X={X}")
        if j in [X-1, X, X+1]:
            crt[i][j] = '#'
        # addx 2 cycle
        if file[-1][0] == 'a':
            if wait < 1:
                wait += 1
            elif wait == 1:
                val = int(file.pop()[5:])
                X += val
                wait = 0

        # noop 1 cycle
        elif file[-1][0] == 'n':
            trash = file.pop() 

        disp_crt()

