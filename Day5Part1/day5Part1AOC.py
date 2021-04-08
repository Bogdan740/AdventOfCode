file = open("day5input.txt","r")
x = file.read()
crudelist = x.split("\n")



rows = []
cols = []

for i in crudelist:
    rows.append(i[0:7])
    cols.append(i[7:10])

seatIdRows = []

for i in rows:
    directions = list(i)
    upper = 127
    lower = 0
    for j in directions:
        if j == "F":
            upper = upper - (((upper-lower)+1)/2)
        elif j == "B":
            lower = lower + (((upper-lower)+1)/2)
    seatIdRows.append(int(lower))

seatIdCols = []
for i in cols:
    directions = list(i)
    upper = 7
    lower = 0
    for j in directions:
        if j == "L":
            upper = upper - (((upper-lower)+1)/2)
        elif j == "R":
            lower = lower + (((upper-lower)+1)/2)
    seatIdCols.append(lower)

seatId = []

for i in range(len(rows)):
    SID = (seatIdRows[i]*8) + seatIdCols[i]
    seatId.append(SID)
print(max(seatId))

    

                           
