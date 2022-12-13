f = open("input.txt", "r")

inp = f.read()
parsed = list(filter(lambda x : x != "$ ls",inp.split("\n")[1:])) # Ignore ls commands because it"s ovious where files have been outputted

directoryTree = ["/"]
directories = {"/" : []}

for i in parsed:
  currentDir = "".join(directoryTree)
  if( i[0] == "$"): # We are being given a command (only 'cd' is left because we filtered out 'ls')
    goTo = i[5:] # Directory to set as current directory
    if(goTo == ".."): # Go backwards one level
      directoryTree.pop()
    else: 
      directoryTree.append(goTo)
      currentDir += goTo
      if(currentDir not in directories):
        directories[currentDir] = []
  else: 
    if(i[0:3] == "dir"): # Directory
      directory = i[4:]
      directories[currentDir].append(currentDir+directory)
    else: # File with given size
      size,_ = i.split()
      directories[currentDir].append(int(size))

total = 0 # Total size for directories <= 100,000

for _ in range(len(directories)):
  for direc in directories:
    files = directories[direc] # All files/directories contained within direc
    if(type(files) != int): # Means we haven't calculated the total size of this directory already
      if(all([type(item) == int for item in files])): # If all items are ints then we can calculate the total size of the directory
        directories[direc] = sumFiles = int(sum(files)) # Calculate the sum of the directory
      else:
        directories[direc] = [directories[k] if type(k) != int and type(directories[k]) == int else k for k in files]
        
used = directories["/"]
unused = 70000000 - used
needed = 30000000 - unused
to_delete_size = sorted( filter(lambda x :x[1] >= needed ,directories.items()), key=lambda x:x[1])[0][1]
print(to_delete_size)

