cinput = open("CodeInputDay1.txt", "r")
a = cinput.read()                                                 
inputList = a.split("\n")
cinput.close()

inputList = [int(i) for i in inputList]
wholeSum = sum(inputList, 0)

print(wholeSum)

 #Code By Bogdan Cuciureanu  # NOTE when using this code don't forget to use your own input
 #Any suggestions on how to make it better will not be ignored, feel free to submit your code :)


    
