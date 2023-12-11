lines = None
with open("test.txt", "r") as fp:
    r = fp.read()
    lines = r.split("\n")
    dim = len(lines)+1

parsed = [list(line) for line in lines]

start_x,start_y = None,None

for i in range(len(parsed)):
    for j in range(len(parsed[0])):
        if(parsed[i][j] == "S"):
            start_x,start_y = j,i
    
nbours = [(-1,0, "right"), (0,1, "up"), (1,0, "left"), (0,-1, "down")]    
can_enter_from_left = {"-", "J", "7"}
can_enter_from_right = {"-", "L", "F"}
can_enter_from_up = {"|", "L", "J"}
can_enter_from_down = {"|", "7", "F"}
can_enter = {"left" : can_enter_from_left, "right" : can_enter_from_right, "down" : can_enter_from_down, "up" : can_enter_from_up}
vertical = set(["J", "7", "L", "F", "|"])
is_vertical = {}

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
    seen = {(x,y) : True}
    while(len(queue) != 0):
        qx,qy,dist = queue.pop(0)
        if((qx,qy) in seen):
            continue
        else:
            if(dist > max_dist):
                max_dist = dist
            seen[(qx,qy)] = True
            if(grid[qy][qx] in vertical):
                is_vertical[(qx,qy)] = True
    
        queue = queue + [(i,j, dist+1) for i,j in get_neighbours(qx,qy,grid)]
    
    return seen    

def get_neighbours2(x,y,grid,seen):
    nbours = [(-1,0), (0,1), (1,0), (0,-1)]  
    touched_edge = False
    to_return_nbours = []
    for nx,ny in nbours:
        cx,cy = x+nx,y+ny
        if(not (0 <= cy < len(grid) and 0<= cx < len(grid[0]))):
            touched_edge = True
            
        if(0 <= cy < len(grid) and 0<= cx < len(grid[0]) and (cx,cy) not in seen):
            to_return_nbours.append((cx,cy))
            
    return touched_edge, to_return_nbours
        
def flood_fill(x,y,grid,seen):
    ff = {(x,y) : True}
    touched_edge_2 = False
    te,queue = get_neighbours2(x,y,grid,seen)
    
    if(te):
        touched_edge_2 = True
    
    while(len(queue) != 0):
        qx,qy = queue.pop(0)
        if((qx,qy) in ff):
            continue
        else:
            ff[(qx,qy)] = True

        te, nbrs = get_neighbours2(qx,qy,grid,seen)
        if(te):
            touched_edge_2 = True
        queue = queue + nbrs
        
    return touched_edge_2, ff

seen = BFS(start_x,start_y, parsed)
total_ff = {}
for i in range(len(parsed)):
    for j in range(len(parsed[0])):
        if((j,i) not in total_ff and (j,i) not in seen):
            inside = len(list(filter(lambda x:(x,i) in seen and (x,i) in is_vertical, range(j,len(parsed[i]))))) %2 != 0
            
            te,ff = flood_fill(j,i,parsed, seen)
            if(te or (not te and not inside)):
                for f in ff:
                    total_ff[f] = False
            else:
                for f in ff:
                    total_ff[f] = True

count = 0
for i,x in enumerate(parsed):
    row = ""
    for j,y in enumerate(parsed[i]):
        if( (j,i) in seen):
            row+=y
        elif( (j,i) in total_ff and total_ff[(j,i)]):
            row+="X"
            count+=1
        else:
            row+="O"
    print(row)

print(count)
    