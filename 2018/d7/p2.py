lines = None
with open("input.txt", "r") as fp:
    lines = fp.read().split("\n")

parsed = [(line.split()[1],line.split()[-3]) for line in lines]
requirement_for = {}
requirements = {}

nodes = set()
for x,y in parsed:
    nodes.add(x)
    nodes.add(y)
    if(x in requirement_for):
        requirement_for[x].append(y)
    else:
        requirement_for[x] = [y]

for y,x in parsed:
    if(x in requirements):
        requirements[x].append(y)
    else:
        requirements[x] = [y]

nodes_with_no_reqs = set([x for x in nodes if x not in requirements])
queue = sorted([x for x in nodes_with_no_reqs])
last_node = [x for x in nodes if x not in requirement_for][0]

is_done = {}
num_workers = 5
time_modifier=60
second = 0
worker_assignments={i : (None,None) for i in range(num_workers)}

while(last_node not in is_done):
    for worker in range(num_workers):
        if(worker_assignments[worker] == (None,None) and len(queue) != 0):
            val = queue.pop(0)
            worker_assignments[worker] = (val, ord(val)-64+time_modifier)
            
    for worker in range(num_workers):
        a,secs_left = worker_assignments[worker]
        if(a == None and secs_left == None):
            continue
        if(secs_left != 1):
            worker_assignments[worker] = (a, secs_left-1)
            continue
        else:
            is_done[a]= True
            worker_assignments[worker] = (None,None)
        
        if(a == last_node):
            is_done[a] = True
            break
        makes_ready = requirement_for[a]
        for k in makes_ready:
            if(all(r in is_done for r in requirements[k]) and k not in queue and k not in is_done):
                queue.append(k)
        queue=sorted(queue)
    
    second+=1

print(second)