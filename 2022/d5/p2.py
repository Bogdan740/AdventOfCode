f = open("input.txt", "r")
inp = f.read()

lines = inp.split('\n')

# Find where stack specification ends and commands start
splitter = lines.index("")

# Split the input into the stack and commands
stackSpec,commands = [lines[i] for i in range(0,splitter-1)], [lines[i] for i in range(splitter+1,len(lines))]
numStacks = int(lines[splitter-1][-2])

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
    
  stacks[to_s-1] += stacks[from_s-1][-num_iters:] # Push to the destination stack in order
  stacks[from_s-1] = stacks[from_s-1][:-num_iters] # Remove the crates from the source stack
  
print("".join([i[-1] for i in stacks]))




