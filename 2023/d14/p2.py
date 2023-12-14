from time import perf_counter

t1 = perf_counter()

lines = None
with open("input.txt", "r") as fp:
    lines = fp.read().split("\n")
    
grid = [list(line) for line in lines]

def cycle(grid):
    # North
    for i,row in enumerate(grid):
        for j,col in enumerate(row):
            if(col == "O"):
                new_row = i-1
                while(grid[new_row][j] == "." and new_row >= 0):
                    new_row-=1
                grid[i][j] = "."
                grid[new_row+1][j] = "O"
    # West
    for i,row in enumerate(grid):
        for j,col in enumerate(row):
            if(col == "O"):
                new_col = j-1
                while(grid[i][new_col] == "." and new_col >= 0):
                    new_col-=1
                grid[i][j] = "."
                grid[i][new_col+1] = "O"
    # South
    for i,row in enumerate(grid[::-1]):
        ii = len(grid)-i-1
        for j,col in enumerate(row):
            if(col == "O"):
                new_row = ii+1
                while(new_row < len(grid) and grid[new_row][j] == "."):
                    new_row+=1
                grid[ii][j] = "."
                grid[new_row-1][j] = "O"
    # West
    for i,row in enumerate(grid):
        for j,col in enumerate(row[::-1]):
            jj = len(row)-j-1
            if(col == "O"):
                new_col = jj+1
                while(new_col < len(row) and grid[i][new_col] == "."):
                    new_col+=1
                grid[i][jj] = "."
                grid[i][new_col-1] = "O"
                

num_cycles = 1000000000
seen = { "\n".join(["".join(row) for row in grid]) : 0}
reverse_seen = { 0 : "\n".join(["".join(row) for row in grid])}
cycle_length = None
start_cycle = None
for i in range(num_cycles):
    cycle(grid)
    ident = "\n".join(["".join(row) for row in grid])
    if(ident in seen):
        cycle_length = (i+1) - seen[ident]
        start_cycle = seen[ident]
        break
    else:
        seen[ident] = i+1
        reverse_seen[i+1] = ident

cycle_calc = (num_cycles-start_cycle+1)%cycle_length
grid = reverse_seen[cycle_calc+start_cycle-1].split("\n")

total_load = 0
for i,row in enumerate(grid):
    for j,col in enumerate(row):
        if(col == "O"):
            total_load += (len(grid)-i)

print(total_load)

t2 = perf_counter()

print(f"Time : {(t2-t1)*1000:.2f}ms")

99291