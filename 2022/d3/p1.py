f = open("input.txt", "r")
inp = f.read()

a = inp.split('\n')
b = list(map(lambda x :(x[:len(x)//2],x[len(x)//2:]),a))

def priority(x):
  o = ord(x)
  if(o > 96):
    return o - 96
  else:
    return o - 38
  
mistakes_sum = 0

for x,y in b:
  mistakes = {}
  for i in x:
    if i in y and i not in mistakes: 
      mistakes_sum += priority(i)
      mistakes[i] = 1
      
print(mistakes_sum)

# RUNNING TIME : O(N^2)
# Note : could easily be improved by implementing a binary search function. You could
# then sort one side of each rucksack and search through it using binary search. This would change
# the running time to O(N log N) but that is a bit overkill here.
  



