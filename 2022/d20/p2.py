f = open("input.txt", "r")
key = 811589153
nums= [ (key*int(x),i) for i,x in enumerate(f.read().split("\n"))]
nums = [ (val%(len(nums)-1),val,i) for (val,i) in nums]

k = nums.copy()
for _ in range(10):
  for (num,realNum,ind) in nums:
    index = k.index((num,realNum,ind))
    newIndex = (index + num  ) % (len(nums)-1)
    k.pop(index)
    k.insert( newIndex,(num,realNum,ind))


k = list(map(lambda x :x[1],k))
numsAfter0 = [k[(k.index(0) + i*1000)%len(k)] for i in range(1,4)]
print(numsAfter0, sum(numsAfter0))
