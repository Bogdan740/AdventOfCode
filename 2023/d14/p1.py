from time import perf_counter

t1 = perf_counter()

lines = None
with open("input.txt", "r") as fp:
    lines = fp.read().split("\n")
    
grid = [list(line) for line in lines]

total_load = 0
for i,row in enumerate(grid):
    for j,col in enumerate(row):
        if(col == "O"):
            new_row = i-1
            while(grid[new_row][j] == "." and new_row >= 0):
                new_row-=1
            new_row = new_row+1
            grid[i][j] = "."
            grid[new_row][j] = "O"
            total_load+=(len(row)-new_row)

print(total_load)

t2 = perf_counter()

print(f"Time : {(t2-t1)*1000:.2f}ms")