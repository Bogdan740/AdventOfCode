lines = None
start_x,start_y = None,None
with open("input.txt", "r") as fp:
    r = fp.read()
    lines = r.split("\n")
    dim = len(lines)+1
    start_y,start_x = r.index("S")//dim, (r.index("S"))%dim

parsed = [list(line) for line in lines]

nbours = [(-1,0, "right"), (0,1, "up"), (1,0, "left"), (0,-1, "down")]    
can_enter_from_left = {"-", "J", "7"}
can_enter_from_right = {"-", "L", "F"}
can_enter_from_up = {"|", "L", "J"}
can_enter_from_down = {"|", "7", "F"}
can_enter = {"left" : can_enter_from_left, "right" : can_enter_from_right, "down" : can_enter_from_down, "up" : can_enter_from_up}

def get_neighbours(x,y,grid):
    to_return_nbours = []
    for nx,ny,direction in nbours:
        ce = can_enter[direction]
        cx,cy = x+nx,y+ny
        
        if(0 <= cy < len(grid) and 0<= cx < len(grid[0]) and grid[cy][cx] in ce):
            to_return_nbours.append((cx,cy))
    return to_return_nbours
        
    
def BFS(x,y,grid):
    queue = [(i,j,1) for i,j in get_neighbours(x,y,grid)]
    max_dist = 1
    seen = {}
    while(len(queue) != 0):
        qx,qy,dist = queue.pop(0)
        if((qx,qy) in seen):
            continue
        else:
            if(dist > max_dist):
                max_dist = dist
            seen[(qx,qy)] = True
    
        queue = queue + [(i,j, dist+1) for i,j in get_neighbours(qx,qy,grid)]
    
    return max_dist    

print(f"{BFS(start_x,start_y, parsed)}")
    