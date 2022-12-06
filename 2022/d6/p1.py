f = open("input.txt", "r")
inp = f.read()

for i in range(len(inp)-3):
  window = inp[i:i+4]
  if(len(set(window)) == 4):
    print(i+4)
    break
  



