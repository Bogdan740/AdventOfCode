lines = None
with open("input.txt", "r") as fp:
    lines = fp.read().split("\n")    

instructions = lines[0]
nodes = [(line.split(" = ")[0],line.split(" = ")[1][1:-1].split(", ")) for line in lines[2:]]
nodes_dict = {a[0] : a[1] for a in nodes}

start = "AAA"
end = "ZZZ"

current = start
instruction_pointer = 0
steps = 0
while(current != end):
    instruction = instructions[instruction_pointer]
    if(instruction == "R"):
        current = nodes_dict[current][1]
    else:
        current = nodes_dict[current][0]
    instruction_pointer = (instruction_pointer+1)%len(instructions)
    steps+=1
print(steps)