file = open("day9input.txt","r")
x = file.read()
crudelist = x.split("\n")

for i in range(len(crudelist)):
    crudelist[i] = int(crudelist[i])

counter1 = 0
counter2 = 25 
for i,num in enumerate(crudelist[25:]):
    preamble = crudelist[counter1:counter2]
    valid = False
    for j in preamble:
        for k in preamble:
            if j+k == num and j!=k:
                valid = True
    if valid == False:
        print(num)
    counter1 +=1
    counter2 +=1
            
            

    
       
