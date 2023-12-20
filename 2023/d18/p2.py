from time import perf_counter

t1 = perf_counter()

lines = []
with open("test.txt", "r") as fp:
    lines = fp.read().split("\n")

int_to_dir = {"0" : "R", "1" : "D", "2" : "L", "3" : "U"}
parsed = [(int(line.split(" ")[2][2:-1][:5], 16),int_to_dir[line.split(" ")[2][2:-1][-1]]) for line in lines]

vertices = set([(0,0)])
x,y = 0,0

directions = {"R" : (1,0), "L" : (-1,0), "U" : (0,-1), "D" : (0,1)}
for length,direction in parsed:
    dx,dy = directions[direction]
    old_x, old_y = x,y
    x+= length * dx
    y+= length * dy
    
    if(dx == 0):
        mi,ma = min(old_y,y),max(old_y, y)
        for i in range(mi, ma+1):
            vertices.add((x,i))
    else:
        mi,ma = min(old_x,x),max(old_x, x)
        for i in range(mi, ma+1):
            vertices.add((i,y))

min_x = min(vertices, key=lambda x:x[0])[0]
max_x = max(vertices, key=lambda x:x[0])[0]
min_y = min(vertices, key=lambda x:x[1])[1]
max_y = max(vertices, key=lambda x:x[1])[1]

check_counter = 0
grid = []
for i in range(min_y,max_y+1):
    print(((i-min_y)/(max_y-min_y))*100)
    row = []
    for j in range(min_x,max_x+1):
        row.append("#" if (j,i) in vertices else ".")
        check_counter+= 1 if (j,i) in vertices else 0
    grid.append(row)

nbours = [(-1,0), (1,0), (0,1), (0,-1)]
def get_nbours(x,y,grid):
    to_return_nbours = []
    for dx, dy in nbours:
        nx,ny = x+dx, y+dy
        
        if(0 <= nx < len(grid[0]) and 0 <= ny < len(grid)):
            to_return_nbours.append((nx,ny))
    return to_return_nbours
        
        
def flood_fill(sx,sy,grid):
    queue = [(sx,sy)]
    counter = 0
    while(len(queue) != 0):
        x,y = queue.pop(0)
        if(grid[y][x] == "#"):
            continue
        else:
            grid[y][x] = "#"
            counter+=1
            queue += get_nbours(x,y,grid)
    return counter

for y,row in enumerate(grid):
    first = False
    ff_done = False
    for x in range(len(row)):
        char = row[x]
        next_is_hash = row[x+1] == "#" if x < len(row)-1 else False
        if(char == "#"):
            if(next_is_hash):
                break
            if(first):
                check_counter += flood_fill(x-1,y,grid)
                ff_done = True
                break
            first = True
    if(ff_done):
        break
        
print(check_counter)

t2 = perf_counter()

print(f"Time : {(t2-t1)*1000:.2f}ms")