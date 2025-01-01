from time import perf_counter

with open("input.txt", "r") as f:
    lines = f.read().split("\n\n")

rules = [list(map(int, r.split("|"))) for r in lines[0].split("\n")]
instructions = [list(map(int,i.split(","))) for i in lines[1].split("\n")]

start = perf_counter()

#  Solution 
LHS = {}

for l,r in rules:
    if l in LHS:
        LHS[l].add(r)
    else:
        LHS[l] = set([r])

total=0
for inst in instructions:
    if(all(l in LHS and r in LHS[l] for l,r in zip(inst[:-1], inst[1:]))):
        total+=int(inst[len(inst)//2])
        
# Output
print(total)
end = perf_counter()


print(f"Time: {(end-start) * 1000:.2f}ms")

# Best time
# 0.30ms