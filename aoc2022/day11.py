# NOTE: remove modulo and div by 3 for part 1
def multby(item:int, op):
    if op =='old':
        return ((item ** 2) % 9699690) // 1 
    return ((item * op) % 9699690) // 1

def addby(item:int, op): return ((item + op) % 9699690) // 1

monkey = {
    'm0': {
        'items': [98, 89, 52],
        'itemOp': [multby, 2],
        'divTest': [5, 6, 1]
    },
    'm1': {
        'items': [57, 95, 80, 92, 57, 78],
        'itemOp': [multby, 13],
        'divTest': [2,2,6]
    },
    'm2': {
        'items': [82, 74, 97, 75, 51, 92, 83],
        'itemOp': [addby, 5],
        'divTest': [19,7,5]
    },
    'm3': {
        'items': [97, 88, 51, 68, 76],
        'itemOp': [addby, 6],
        'divTest': [7,0,4]
    },
    'm4': {
        'items': [63],
        'itemOp': [addby, 1],
        'divTest': [17,0,1],
    },
    'm5': {
        'items': [94, 91, 51, 63],
        'itemOp': [addby, 4],
        'divTest': [13,4,3]
    },
    'm6': {
        'items': [61, 54, 94, 71, 74, 68, 98, 83],
        'itemOp': [addby, 2],
        'divTest': [3,2,7]
    },
    'm7': {
        'items': [90, 56],
        'itemOp': [multby, 'old'],
        'divTest': [11,3,5]
    }
}


inspect_counter = [0 for i in range(8)]
for i in range(10000):
    for j in range(8):
        curr_m = monkey['m'+str(j)]
        curr_itemlist = curr_m['items']
        while len(curr_itemlist) > 0:
            inspect_counter[j] += 1
            item = curr_itemlist.pop()
            op = curr_m['itemOp']
            new_val = op[0](item, op[1]) 
            if new_val % curr_m['divTest'][0] == 0:
                monkey['m'+str(curr_m['divTest'][1])]['items'].append(new_val)
            else:
                monkey['m'+str(curr_m['divTest'][2])]['items'].append(new_val)


print(inspect_counter)
inspect_counter.sort()
print(inspect_counter)
top = inspect_counter.pop()
sec = inspect_counter.pop()
print(f"top={top}, sec={sec}, monkey_business={top*sec}")
