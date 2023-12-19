from time import perf_counter

t1 = perf_counter()

lines = None
with open("test.txt", "r") as fp:
    lines = fp.read().split("\n")

UP, RIGHT, DOWN, LEFT = 0,1,2,3

heat_values = [list(map(int,line)) for line in lines]

# Here we store the least heat loss while getting to this path
grid = [[(float("inf"), None, None) for _ in range(len(heat_values[0]))] for _ in range(len(heat_values))]

nbours = [(-1,0, LEFT), (1,0, RIGHT), (0,1, DOWN), (0,-1, UP)]
def get_nbours(x,y,num_times_same_dir,cur_dir,heat_lost,grid):
    to_return_nbours = []
    must_change_dir = num_times_same_dir == 2
    allowed_dirs = set([(cur_dir+1)%4,  (cur_dir-1)%4]) if must_change_dir else set([UP, RIGHT, DOWN, LEFT])
    for i,j,direction in [nbour for nbour in nbours if nbour[2] in allowed_dirs]:
        nx,ny = x+i, y+j
        if(not (0 <= nx < len(grid) and 0 <= ny < len(grid[0]))):
            continue

        to_return_nbours.append((nx, ny, direction, 0 if direction != cur_dir else num_times_same_dir+1, heat_lost+heat_values[ny][nx],x,y))

    return to_return_nbours

dir_symbol = {RIGHT : ">", LEFT : "<", UP : "^", DOWN : "v"}  
tx,ty = (len(grid[0])-1, len(grid)-1)
def BFS(sx,sy,grid):
    # x, y, cur_dir, num_times_same_dir, heat_lost, came_from_x, came_from_y
    queue = [(sx,sy,0,0,0,None,None)]
    seen_before = set()
    while(len(queue) != 0):
        queue = sorted(queue, key=lambda x:x[4])
        x,y,direction,num_times_same_dir,heat_lost,came_from_x,came_from_y = queue.pop(0)
        ident = (x,y,direction,num_times_same_dir)
        if(ident in seen_before):
            continue
        else:
            seen_before.add(ident)
            opposite_direction = (direction+2)%4
            seen_before.add((x,y,opposite_direction,0))
            seen_before.add((x,y,opposite_direction,1))
            seen_before.add((x,y,opposite_direction,2))
        
        if(grid[y][x][0] > heat_lost):
            grid[y][x] = (heat_lost, came_from_x, came_from_y, direction)
        queue += get_nbours(x,y,num_times_same_dir,direction,heat_lost,grid)
    
        
BFS(0,0,grid)

path = set()
path_with_dir = {}
final_val = grid[-1][-1]
x,y = final_val[1], final_val[2]
while(x != None and y != None):
    path_with_dir[(x,y)] = final_val[3]
    path.add((x,y))
    final_val = grid[y][x]
    x,y = final_val[1], final_val[2]

heat_lost = 0

for i in range(len(grid)):
    row = ""
    for j in range(len(grid[0])):
        row += dir_symbol[path_with_dir[(j,i)]] if (j,i) in path else "."
        heat_lost += heat_values[j][i] if (j,i) in path else 0
    print(row)
    
print(heat_lost + heat_values[-1][-1])
print(grid[-1][-1][0])
t2 = perf_counter()
print(f"Time : {(t2-t1)*1000:.2f}ms")

# 850 -- TOO HIGH
# 663 -- TOO LOW