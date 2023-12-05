lines = None
with open("input.txt", "r") as fp:
    lines = fp.read().split("\n")

coords = [ tuple(map(int,line.split(", "))) for line in lines]

min_x = min(map(lambda x:x[0], coords))
max_x = max(map(lambda x:x[0], coords))
min_y = min(map(lambda x:x[1], coords))
max_y = max(map(lambda x:x[1], coords))

# Transform the coordinates around 0,0
coords = [(x-min_x,y-min_y) for x,y in coords]

c_map = {coords[i]:i for i in range(len(coords))}

grid = [[(".",0, None) for _ in range(min_x, max_x+1)] for _ in range(min_y, max_y+1)]

for y in range(len(grid)):
    for x in range(len(grid[0])):
        if((x,y) in coords):
            grid[y][x] = ("x",0, c_map[(x,y)])

def get_neighbours(x,y):
    nbours = [(1,0), (-1,0), (0,1), (0,-1)]
    return [(x+i, y+j) for i,j in nbours]
    
def BFS(x,y, grid, root):
    queue = [(k,1) for k in get_neighbours(x,y)]
    seen = {(x,y) : True}
    while(len(queue)!=0):
        (cx,cy),dist = queue.pop(0)
        # Already seen before check
        if((cx,cy) in seen):
            continue
        else:
            seen[(cx,cy)] = True
    
        # Out of bounds check
        if(not 0<= cx < len(grid[0]) or not 0<= cy < len(grid)):
            continue
        else:
            drawing,val,_ = grid[cy][cx]
            grid[cy][cx] = (drawing, dist + val,root) 
            queue=queue+[(k, dist+1) for k in get_neighbours(cx,cy)]
        
for x,y in coords:
    BFS(x,y,grid, c_map[(x,y)])

# Find all areas coresponding to each point
flat_list_grid = [item for sublist in grid for item in sublist]
areas = [x[2] for x in flat_list_grid]
areas_dict = {c_map[x] : areas.count(c_map[x]) for x in c_map}

# Find all areas which are infinite
is_infinite = {}
# Check the first and last rows, and the first and last columns
for list_to_check in grid[0],grid[-1],[grid[x][0] for x in range(len(grid))],[grid[x][-1] for x in range(len(grid))]:
    for _,_,indent in list_to_check:
        is_infinite[indent] = True

# Find the largest area which is not infinite

counter = 0
for i in grid:
    for k in [j[1] for j in i]:
        if(k < 10000):
            counter+=1
print(counter)

