lines = None
with open("input.txt", "r") as fp:
    lines = fp.read().split("\n")

grid = [list(line) for line in lines]

empty_rows = set()
empty_cols = set()

for i,row in enumerate(grid):
    if(all(x == "." for x in row)):
        empty_rows.add(i)
        
for i in range(len(grid[0])):
    all_dots = True
    for j in range(len(grid)):
        if(grid[j][i]) != ".":
            all_dots = False
            break
    if(all_dots):
        empty_cols.add(i)

empty_rows = sorted(empty_rows)
empty_cols = sorted(empty_cols)

galaxies = set()

for i in range(len(grid)):
    for j,val in enumerate(grid[i]):
        if(val == "#" and (j,i) not in galaxies):
            galaxies.add((j,i))

min_dist_sums = 0
seen_before = set()
multiplier = 2
for x,y in galaxies:
    for i,j in galaxies:
        if((x,y) != (i,j) and ((x,y),(i,j)) not in seen_before):
            
            extra_cols_between = len([col for col in empty_cols if x < col < i or i < col < x])
            
            extra_rows_between = len([row for row in empty_rows if y < row < j or j < row < y])
            
            min_dist_sums+=abs(y-j)+extra_rows_between*(multiplier-1)+abs(x-i)+extra_cols_between*(multiplier-1)
                        
            seen_before.add(((x,y),(i,j)))
            seen_before.add(((i,j),(x,y)))
    
print(min_dist_sums)