lines = None
with open("input.txt") as fp:
    lines = fp.read().split("\n")

parsed = [list(line) for line in lines]

neighbours = [(1,1), (1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1), (0,1)]

def is_symbol(c):
    return not c.isdigit() and c!="."

def get_neighbouring_symbols(i,j):
    to_return = False
    neighbouring_symbols = []
    for n in neighbours:
        ni = i+n[0]
        nj = j+n[1]
        if(0<= ni < len(lines) and 0<= nj < len(lines[0]) and is_symbol(lines[ni][nj])):
            neighbouring_symbols.append((ni, nj,lines[ni][nj] ))
            to_return = True
    return to_return,set(neighbouring_symbols)
        
a = {}

for k,line in enumerate(lines):
    i = 0
    while(i < len(line)):
        c = line[i]
        if(c.isdigit()):
            is_next_to_symbol = False
            digit_holder = ""
            neighbouring_symbols = []
            while(c.isdigit()):
                has_ns,ns = get_neighbouring_symbols(k,i) 
                if(has_ns):
                    neighbouring_symbols+=ns
                    is_next_to_symbol = True
                digit_holder+=c
                i+=1
                c=line[i] if i < len(line) else ""
            if(is_next_to_symbol):
                neighbouring_symbols = set(neighbouring_symbols)
                for ns in neighbouring_symbols:
                    if(ns in a):
                        a[ns].append(int(digit_holder))
                    else:
                        a[ns] = [int(digit_holder)]
        else:
            i+=1

total = 0

for k in a:
    _,_,s = k
    if(s == "*" and len(a[k]) == 2):
        total += a[k][0] * a[k][1]

print(total)