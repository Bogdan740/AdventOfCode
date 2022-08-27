import re

file = open("CodeInputDay2Part2.txt" , "r")
a = file.read()
input_lines = a.split("\n")
file.close()

position = 0
TimesSeen = {0}

sum = 0
while True:
    line = input_lines[position]
    num = line.rstrip()
    sum += int(num)
    if sum in TimesSeen:
        print(sum)
        break
    else:
        TimesSeen.add(sum)
    position = (position + 1) % len(input_lines)

    
#Code By Bogdan Cuciureanu  # NOTE when using this code don't forget to use your own input
#Any suggestions on how to make it better will not be ignored, feel free to submit your code :)
        
        
    
