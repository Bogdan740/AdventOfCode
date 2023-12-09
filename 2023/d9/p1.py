lines = []
with open("input.txt", "r") as fp:
    lines = fp.read().split("\n")

parsed = [[int(i) for i in line.split()] for line in lines]

def get_next(l):
    if(all(l[0] == i for i in l)):
        return l[0]
    
    differences = [i-j for (i,j) in zip(l[1:],l)]
    next = get_next(differences)
    return l[-1] + next
    
nexts_total = sum([get_next(i) for i in parsed])
print(nexts_total)