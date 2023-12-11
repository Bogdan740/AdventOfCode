lines = None
with open("input.txt", "r") as fp:
    r = fp.read()
    lines = r.split("\n")
    dim = len(lines)+1

parsed = [list(line) for line in lines]

start_x,start_y = None,None

for i in range(len(parsed)):
    for j in range(len(parsed[0])):
        if(parsed[i][j] == "S"):
            start_x,start_y = j,i
    
nbours = [(-1,0, "left"), (0,1, "down"), (1,0, "right"), (0,-1, "up")]    
can_enter_from_left = {"-", "J", "7"}
can_enter_from_right = {"-", "L", "F"}
can_enter_from_up = {"|", "L", "J"}
can_enter_from_down = {"|", "7", "F"}
can_enter = {"right" : can_enter_from_left, "left" : can_enter_from_right, "up" : can_enter_from_down, "down" : can_enter_from_up}
left = (-1,0)
right = (1,0)
up = (0,1)
down = (0,-1)

vertical = {"J", "7", "L", "F", "|"}
is_vertical = {}

can_go_towards = {"J" : [(-1,0, "left"),(0,-1, "up") ], "7" : [(-1,0, "left"),(0,1, "down")], "|" : [(0,-1, "up"),(0,1, "down")], "-" : [(-1,0, "left"), (1,0, "right")], "L" : [(1,0, "right"), (0,-1, "up")], "F" : [(0,1, "down"),(1,0, "right")],"S" : [(-1,0, "left"),(0,1, "down")]}

def get_neighbours(x,y,grid):
    to_return_nbours = []
    for nx,ny,direction in can_go_towards[grid[y][x]]:
        ce = can_enter[direction]
        cx,cy = x+nx,y+ny
        
        if(0 <= cy < len(grid) and 0<= cx < len(grid[0]) and grid[cy][cx] in ce):
            to_return_nbours.append((cx,cy))
    return to_return_nbours
        

def BFS(x,y,grid):
    queue = [(i,j,1) for i,j in get_neighbours(x,y,grid)]
    seen = {(x,y) : True}
    while(len(queue) != 0):
        qx,qy,dist = queue.pop(0)
        if((qx,qy) in seen):
            continue
        else:
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
            to_right = [l if (j+1+ind,i) in seen else "." for ind,l in enumerate(parsed[i][j+1:])]
            pointer = 0
            counter = 0
            while(pointer < len(to_right)):
                character = to_right[pointer]
                oc = character
                ceuoc = character in can_enter_from_up
                cedoc = character in can_enter_from_down
                if(character in can_enter_from_right):
                    pointer+=1
                    if(pointer >= len(to_right)):
                        continue
                    character = to_right[pointer]
                    while(character == "-" and pointer < len(to_right)):
                        pointer+=1
                        character = to_right[pointer]
                    if(character in can_enter_from_left):
                        if(ceuoc and character in can_enter_from_up or cedoc and character in can_enter_from_down):
                            counter+=0
                        elif(ceuoc and character in can_enter_from_down or cedoc and character in can_enter_from_up):
                            counter+=1
                    else:
                        counter+=2
                else:
                    if(character in vertical):
                        counter+=1
                pointer+=1

            inside = counter % 2 != 0
            
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
        if( (j,i) in total_ff and total_ff[(j,i)]):
            row+="X"
            count+=1
        elif((j,i) in seen):
            row+=y
        else:
            row+="O"
    print(row)

print(count)
    