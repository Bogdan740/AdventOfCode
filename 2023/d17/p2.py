from time import perf_counter
import heapq

t1 = perf_counter()

lines = None
with open("input.txt", "r") as fp:
    lines = fp.read().split("\n")

heat_values = [list(map(int,line)) for line in lines]

grid = [[float("inf") for _ in range(len(heat_values[0]))] for _ in range(len(heat_values))]

UP, RIGHT, DOWN, LEFT = 0,1,2,3

dir_move = {RIGHT : (1,0), LEFT : (-1,0), UP : (0,-1), DOWN : (0,1)}
nbours = [(1,0,RIGHT), (-1,0,LEFT), (0,1,DOWN), (0,-1,UP)]
def get_nbours(x,y, current_direction, ntsd,heat_value,queue):
    if(ntsd == 9):
        turn_1 = (current_direction+1)%4
        turn_2 = (current_direction-1)%4
        for (i,j),direction in [(dir_move[turn_1],turn_1),(dir_move[turn_2],turn_2)]:
            nx,ny = x+i,y+j
            if(not (0 <= nx < len(grid[0]) and 0 <= ny < len(grid))):
                continue
            heapq.heappush(queue,(heat_value + heat_values[ny][nx],nx,ny,direction,0))
    else:
        for i,j,direction in nbours:
            if(current_direction != None and direction == (current_direction+2)%4):
                continue
            nx,ny = x+i,y+j
            if(not (0 <= nx < len(grid[0]) and 0 <= ny < len(grid))):
                continue
            if( (current_direction == direction or ntsd >= 3 or ntsd == -1)):
                heapq.heappush(queue,(heat_value + heat_values[ny][nx],nx,ny,direction, ntsd+1 if current_direction == direction else 0))


queue = [(-1,0,0,None,-1)]
seen = set()
while(len(queue) != 0):
    heat_value,x,y,direction,ntsd = heapq.heappop(queue)
    ident = (x,y,direction,ntsd)
    if(grid[y][x] > heat_value and ntsd >= 3):
        grid[y][x] =heat_value
    if(ident in seen):
        continue
    else:
        seen.add(ident)
    
    get_nbours(x,y,direction,ntsd,heat_value,queue)
        

print(grid[-1][-1]+1)

t2 = perf_counter()

# for row in grid:
#     rstring = ""
#     for i in row:
#         x = str(i)
#         if(x == "inf"):
#             rstring += "-1 "
#         elif(len(x) == 1):
#             rstring += f"0{x} "
#         else:
#             rstring += f"{x} "
#     print(rstring)
            

print(f"Time : {(t2-t1)*1000:.2f}ms")

# 796 too high