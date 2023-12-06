lines = None
with open("input.txt", "r") as fp:
    lines = fp.read().split("\n")

parsed = [(line.split()[1],line.split()[-3]) for line in lines]
requirement_for = {}
requirements = {}

for x,y in parsed:
    if(x in requirement_for):
        requirement_for[x].append(y)
    else:
        requirement_for[x] = [y]

for y,x in parsed:
    if(x in requirements):
        requirements[x].append(y)
    else:
        requirements[x] = [y]

seen = {}
last = [x for x in [item for sublist in parsed for item in sublist] if x not in requirement_for][0]

with_no_reqs = set([x for x in [item for sublist in parsed for item in sublist] if x not in requirements])
is_ready = {x : True for x in with_no_reqs}

queue = sorted([x for x in with_no_reqs])

order = ""
while(len(queue) != 0):
    a = queue.pop(0)
    seen[a] = True
    if(a not in requirement_for):
        continue
    order+=a
    makes_ready = requirement_for[a]
    for k in makes_ready:
        if(all(r in is_ready for r in requirements[k]) and k not in is_ready ):
            is_ready[k] = True
            queue.append(k)
    queue=sorted(queue)

order+=last

print(order)
