cinput = open("CodeInputDay1.txt", "r")
a = cinput.read()
inputList = a.split("\n")
cinput.close()

inputList = [int(i) for i in inputList]
wholeSum = sum(inputList, 0)

print(wholeSum)




    
