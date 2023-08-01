p1 = False
file = open("day9in.txt").readlines()
tail_posistions = [[0,0]]
tails = [[0,0] for a in range(9)]
Head = [0,0]
true_tail = tails[0 if p1 else 8]
dd = {'U':[1,1], 'D':[1,-1], 'R':[0,1], 'L':[0,-1]}
for line in file:
    n = int(line[2:])
    move = dd[line[0]]
    for i in range(n):
        Head[move[0]] += move[1]
        copy = list(Head)
        for iterTail in tails:
            x_diff = copy[0] - iterTail[0]
            y_diff = copy[1] - iterTail[1]
            if not (abs(x_diff) <=1 and abs(y_diff) <= 1):
                if x_diff != 0: iterTail[0] += int(abs(x_diff)/x_diff)
                if y_diff != 0: iterTail[1] += int(abs(y_diff)/y_diff)
            copy = list(iterTail)
            if p1: break
        if list(true_tail) not in tail_posistions: tail_posistions.append(list(true_tail))
print(len(tail_posistions))