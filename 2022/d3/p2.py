f = open("input.txt", "r")
inp = f.read()

a = inp.split('\n')

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1
  
def priority(x):
  o = ord(x)
  if(o > 96):
    return o - 96
  else:
    return o - 38

k = [[a[i],a[i+1],a[i+2]] for i in range(0,len(a),3)]
k = list(map(lambda x: list(map( lambda y: list(map(priority, y)),x)),k))

badges = []

for group in k:
  luggage1 = group[0]
  luggage2 = sorted(group[1])
  luggage3 = sorted(group[2])
  for item in luggage1:
    if(binary_search(luggage2,item) != -1 and binary_search(luggage3, item) != -1):
      badges.append(item)
      break    
    
print(sum(badges))


