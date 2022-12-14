#! usr/bin/python3

def topVis(curr_row:int, curr_col:int, h:int, grid):
    count = 0
    rr = [i for i in range(0, curr_row)]
    rr = rr[::-1]
    for i in rr:
        if grid[i][curr_col] >= h:
            count += 1
            break #return False for PART 1
        else:
            count += 1
    return count #True

def botVis(n_rows:int, curr_col:int, curr_row:int, h:int, grid):
    count = 0
    for i in range(curr_row+1, n_rows):
        if grid[i][curr_col] >= h:
            count += 1
            break #return False for PART 1
        else:
            count += 1
    return count #True for part1 

def leftVis(curr_row:int, curr_col:int, h:int, grid):
    count = 0
    rr = [i for i in range(0, curr_col)]
    rr = rr[::-1]
    for j in rr:
        if grid[curr_row][j] >= h:
            count += 1
            break #return False for PART 1
        else:
            count += 1
    return count #True for part1 

def rightVis(n_cols:int, curr_row:int, curr_col:int, h:int, grid):
    count = 0
    for j in range(curr_col+1, n_cols):
        if grid[curr_row][j] >= h:
            count += 1
            break #return False for PART 1
        else:
            count += 1
    return count #True for PART 1

def sidesVisible(n_cols:int, n_rows:int, curr_row:int, curr_col:int, h:int, grid) -> bool:
    l = topVis(curr_row, curr_col, h, grid)
    m = botVis(n_rows, curr_col, curr_row, h, grid) 
    n = leftVis(curr_row, curr_col, h, grid) 
    o = rightVis(n_cols, curr_row, curr_col, h, grid)
    #print(f"top={l}::lft={n}::ryt={o}::dwn={m}::height={h}")
    
    
    #PART1 return l + m + n + o
    return l * m * n * o
    


def print_grid(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            print(f"{grid[i][j]}", end = " ")
        print("\n")

with open('day8in.txt', 'r') as file:
    grid = [[int(i) for i in l.rstrip()] for l in file.readlines()] 
    n_cols = len(grid[0])
    n_rows = len(grid)
    total_vis = (n_cols * 2) + (n_rows-2) * 2 
    
    best_score = 0

    for i in range(1, n_cols-1):
        for j in range(1, n_rows-1):
            #x = sidesVisible(n_cols, n_rows, i, j, grid[i][j], grid)
            #print(f"deb::{x}::{i}::{j}::{grid[i][j]}")

            # grid_dict[str(sidesVisible(n_cols, n_rows, i, j, grid[i][j], grid))] = (i, j)
            x = sidesVisible(n_cols, n_rows, i, j, grid[i][j], grid)
            if best_score < x:
                best_score = x
            # NOTE: for PART 1
            # if sidesVisible(n_cols, n_rows, i, j, grid[i][j], grid):
            #     total_vis += 1

    #print_grid(grid)
    #print(sidesVisible(n_cols, n_rows, 2, 1, 5, grid))
    #best_score = max([int(i) for i in grid_dict.keys()])
    print(best_score)
    #print(total_vis)
