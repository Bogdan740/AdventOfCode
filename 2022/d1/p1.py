f = open("input.txt", "r")
inp = f.read()

food = inp.split('\n')
elfs = []
holder = []
for f in food:
  if(f == ''):
    elfs.append(sum(map(int,holder)))
    holder = []
  else:
    holder.append(f)
print(max(elfs))
  




