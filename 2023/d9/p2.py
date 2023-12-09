lines = []
with open("input.txt", "r") as fp:
    lines = fp.read().split("\n")

parsed = [[int(i) for i in line.split()] for line in lines]

def get_previous(l):
    if(all(l[0] == i for i in l)):
        return l[0]
    
    differences = [i-j for (i,j) in zip(l[1:],l)]
    next = get_previous(differences)
    return l[0] - next
    
nexts_total = sum([get_previous(i) for i in parsed])
print(nexts_total)