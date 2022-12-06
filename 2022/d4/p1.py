f = open("input.txt", "r")
inp = f.read()

a = list(map(lambda x:x.split(","),inp.split('\n')))

counter = 0
for r in a:
  x,y = map(int,r[0].split("-"))
  a,b = map(int,r[1].split("-"))
  if(x <= a <= b <= y or a <=x<=y<=b):
    counter+=1
print(counter)