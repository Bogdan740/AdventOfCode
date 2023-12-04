lines = None
with open("input.txt") as fp:
    lines = fp.read()

def reduce(lines):
    i = len(lines)-1
    while(i>0):
        x = lines[i]
        y = lines[i-1]    
        if(x.lower() == y.lower() and x.islower()+y.islower() == 1 and i>0):
            while(x.lower() == y.lower() and x.islower()+y.islower() == 1 and i>0):                
                lines = lines[:i-1] + lines[i+1:]
                i-=1
                if(i==len(lines)):
                    i-=1
                x = lines[i]
                y = lines[i-1]
        else:
            i-=1
    return len(lines)

min_found = float('inf')
for l in "abcdefghijklmnopqrstuvwxyz":
    filtered = lines.replace(l,"").replace(l.upper(),"")
    a = reduce(filtered)
    if(a < min_found):
        min_found=a

print(min_found)
