f = open("input.txt", "r")
inp = f.read()

parsed = inp.split('\n')

# Find where stack specification ends and commands start
splitter = parsed.index("")

# Split the input into the stack and commands
stackSpec,commands = [parsed[i] for i in range(0,splitter-1)], [parsed[i] for i in range(splitter+1,len(parsed))]
numStacks = int(parsed[splitter-1][-2])

# Initiate stack data structure
stacks = [[] for i in range(numStacks)]

# Load stacks into data structure
for i in stackSpec:
  counter = 0;
  for j in range(0,len(i),4):
    if i[j+1] != ' ':
      stacks[counter].insert(0,i[j+1]) 
    counter+=1

# Run all commands on the stack
for command in commands:
  # Extract the numbers out of the command
  # The 1st number indicates how many moves to make
  # The 2nd number indicates from which stack to pop
  # The 3rd number indicates onto which stack to push
  num_iters,from_s,to_s = map(int,filter(lambda x:x.isnumeric(), command.split())) 
  for i in range(num_iters):
    stacks[to_s-1].append(stacks[from_s-1].pop())

print("".join([i[-1] for i in stacks]))




