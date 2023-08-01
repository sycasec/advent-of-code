import re
 
data=dict()
act_key=""
same_c=[]
same_l=[]
 
with open("day7in.txt") as file:
    for line in file:
        n=1
        while re.match("^dir.*",line) and line.split()[1] in same_l:
            x=line.split()
            x[1]=x[1]+str(n)
            line=" ".join(x)
 
        while re.match("^\$\scd\s[^\.].*",line) and line.split()[2] in same_c:
            x=line.split()
            x[2]=x[2]+str(n)
            line=" ".join(x)
 
        if re.match("^\$\scd\s[^\.].*",line):
            act_key=line.split()[2]
            data[act_key]=[0]
            same_c.append(line.split()[2])
        elif re.match("^[^\$].*",line):
            if line.split()[0].isnumeric():
                data[act_key][0]+=int(line.split()[0])
            else:
                data[act_key].append(line.split()[1])
                same_l.append(line.split()[1])
 
for i in list(data.keys())[::-1]:
    if len(data[i])>1:
        for j in range(len(data[i][1:])):
            subdir=data[i][j+1]
            data[i][0]+=int(data[subdir][0])
        
        del(data[i][1:])
 
print("Part 1:",sum([size[0] for size in data.values() if size[0]<=100000]))
print("Part 2:", sorted([data[size][0] for size in data.keys() if 70000000-data["/"][0]+data[size][0]>=30000000])[0])