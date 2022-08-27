f = open("puzzleinput.txt", "r")
testData = f.read()
f.close()

inputArr = list(map(int,testData.split(",")))

lowestFuelCost = float("inf")

for i in range(max(inputArr)):
  total = 0
  for j in inputArr:
    total += abs(j-i)
  if total < lowestFuelCost:
    lowestFuelCost = total
    
lowestFuelCost2 = float("inf")

for i in range(max(inputArr)):
  total = 0
  for j in inputArr:
    total += sum(range(abs(j-i)+1))
  if total < lowestFuelCost2:
    lowestFuelCost2 = total

print("Day 1",lowestFuelCost)
print("Day 2",lowestFuelCost2)
