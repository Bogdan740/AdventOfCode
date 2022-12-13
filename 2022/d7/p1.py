f = open("input.txt", "r")

inp = f.read()
# tried : 1091949, 1113904
parsed = list(filter(lambda x : x != "$ ls",inp.split("\n")[1:])) # Ignore ls commands because it"s ovious where files have been outputted

directoryTree = ["/"]
currentDir = "/"
directories = {("/",1) : []}
depth = 1

print("Status : ", directoryTree,currentDir,depth)
for i in parsed:
  if( i[0] == "$"): # We are being given a command (only 'cd' is left because we filtered out 'ls')
    print(i, end = ' | ')
    goTo = i[5:] # Directory to set as current directory
    if(goTo == ".."): # Go backwards one level
      directoryTree.pop()
      depth -=1
      currentDir = directoryTree[-1]
      print("Status : ", directoryTree,currentDir,depth)
    else: 
      currentDir = goTo
      directoryTree.append(goTo)
      depth +=1
      print("Status : ", directoryTree,currentDir,depth)
      if((currentDir,depth) not in directories):
        directories[(currentDir,depth)] = []
  else: 
    if(i[0:3] == "dir"): # Directory
      directory = i[4:]
      directories[(currentDir,depth)].append((directory,depth+1))
    else: # File with given size
      size = i.split()[0]
      directories[(currentDir,depth)].append(int(size))

total = 0 # Total size for directories <= 100,000

for _ in range(len(directories)+1):
  for direc in directories:
    files = directories[direc] # All files/directories contained within direc
    if(type(files) != int): # Means we haven"t calculated the total size of this directory already
      if(all(type(item) == int for item in files)): # If all items are ints then we can calculate the total size of the directory
        directories[direc] = sumFiles = int(sum(files)) # Calculate the sum of the directory
        if(sumFiles <= 100000): # If the sum is <= 100,000 tw2hen add it to the total
          # print(direc,sizes[direc])
          total += sumFiles 
      else:
        directories[direc] = [directories[k] if type(k) != int and type(directories[k]) == int else k for k in files]


# for i in directories:
#   print(i,directories[i])


