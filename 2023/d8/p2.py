from math import lcm

lines = None
with open("input.txt", "r") as fp:
    lines = fp.read().split("\n")    

instructions = lines[0]
node_path = [(line.split(" = ")[0],line.split(" = ")[1][1:-1].split(", ")) for line in lines[2:]]
nodes = [a[0] for a in node_path]
nodes_dict = {a[0] : a[1] for a in node_path}

starts = [node for node in nodes if node.endswith("A")]
ends = {node : True for node in nodes if node.endswith("Z")}

loop_numbers = []
for node in starts:
    current = node
    instruction_pointer = 0
    steps = 0
    while(current not in ends):
        instruction = instructions[instruction_pointer]
        if(instruction == "R"):
            current = nodes_dict[current][1]
        else:
            current = nodes_dict[current][0]
        instruction_pointer = (instruction_pointer+1)%len(instructions)
        steps+=1
        if(current in ends):
            loop_numbers.append(steps)

print(lcm(*loop_numbers))
