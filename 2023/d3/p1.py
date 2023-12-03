lines = None
with open("input.txt") as fp:
    lines = fp.read().split("\n")

parsed = [list(line) for line in lines]

neighbours = [(1,1), (1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1), (0,1)]

def is_symbol(c):
    return not c.isdigit() and c!="."
    
def has_neighbouring_symbol(i,j):
    for n in neighbours:
        ni = i+n[0]
        nj = j+n[1]
        if(0<= ni < len(lines) and 0<= nj < len(lines[0]) and is_symbol(lines[ni][nj])):
            return True
    return False
        
total = 0
for k,line in enumerate(lines):
    i = 0
    while(i < len(line)):
        c = line[i]
        if(c.isdigit()):
            is_next_to_symbol = False
            digit_holder = ""
            while(c.isdigit()):
                if(has_neighbouring_symbol(k,i)):
                    is_next_to_symbol = True
                digit_holder+=c
                i+=1
                c=line[i] if i < len(line) else ""
            if(is_next_to_symbol):
                total+=int(digit_holder)  
        else:
            i+=1

print(total)