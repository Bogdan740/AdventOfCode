f = open("input.txt", "r")
nums= [ (int(x),i) for i,x in enumerate(f.read().split("\n"))]
# nums= [ (int(x),i) for i,x in enumerate([0,-4])]

k = nums.copy()

for (num,ind) in nums:
  index = k.index((num,ind))
  newIndex = (index + num  ) % (len(nums)-1)
  k.pop(index)
  k.insert( newIndex,(num,ind))


k = list(map(lambda x :x[0],k))
numsAfter0 = [k[(k.index(0) + i*1000)%len(k)] for i in range(1,4)]
print(numsAfter0, sum(numsAfter0))
