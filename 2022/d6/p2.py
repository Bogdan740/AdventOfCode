f = open("input.txt", "r")
inp = f.read()

for i in range(len(inp)-3):
  window = inp[i:i+14]
  if(len(set(window)) == 14):
    print(i+14)
    break
  



