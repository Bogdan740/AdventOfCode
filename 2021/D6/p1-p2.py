f = open("testdata.txt", "r")
testData = f.read()
f.close()

inputArr = list(map(int,testData.split(",")))


def calculateTotalFishAfterDays(days):
  timerCounter = [0]*9
  for i in inputArr:
    timerCounter[i]+=1
    
  for i in range(days):
    fishAboutToGiveBirth = timerCounter[0]
    for i in range(len(timerCounter)-1):
      timerCounter[i] = timerCounter[i+1]
    timerCounter[len(timerCounter)-1] = fishAboutToGiveBirth
    timerCounter[6]+=fishAboutToGiveBirth
  
  print("Total number of fish after {} days is : {}".format(days,sum(timerCounter)))
  
calculateTotalFishAfterDays(80)
calculateTotalFishAfterDays(256)