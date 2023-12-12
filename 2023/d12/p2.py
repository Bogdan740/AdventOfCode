lines = None
with open("input.txt", "r") as fp:
    lines = fp.read().split("\n")

parsed = [[line.split()[0],[int(i) for i in line.split()[1].split(",")]] for line in lines]
parsed = [("?".join(line for _ in range(5)), req*5) for line, req in parsed]

seen_before = {}
def DP(line, requirements, counter):   
    ident = line+str(requirements)
    if(ident in seen_before):
        return seen_before[ident]
        
    all_dots = all(i != "#" for i in line)
    if(len(requirements) == 0 ):
        seen_before[ident] = counter+1 if all_dots else 0 
        return counter+1 if all_dots else 0 
    elif(len(line) == 0):
        return 0
    
    to_return = None
    
    requirement = requirements[0]
    if(len(line) < requirement):
        seen_before[ident] = 0
        return 0
    sample = line[:requirement]
    if(all(s=="#" for s in sample) and not (len(line)>requirement and line[requirement]=="#")):
        to_return = DP(line[requirement+1:], requirements[1:], counter)
    
    elif(all(s!="." for s in sample) and not (len(line)>requirement and line[requirement]=="#")):
        if(sample[0] == "#"):
            to_return = DP(line[requirement+1:],requirements[1:],counter)
        else:
            to_return = DP(line[requirement+1:],requirements[1:],counter) + DP(line[1:],requirements,counter)
    
    else:
        if(len(line) != 0 and line[0] == "#"):
            seen_before[ident] = 0
            return 0
        i = 1
        while(i < len(line) and line[i] == "."):
            i+=1
        to_return = DP(line[i:],requirements, counter)
    
    seen_before[ident] = to_return
    return to_return

sum_possibilitites = 0
for line, ex in parsed:
    sum_possibilitites += DP(line, ex, 0)

print(sum_possibilitites)