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
def get_nbours(x,y, current_direction, num_times_same_direction,heat_value):
    to_return_nbours = []
    if(num_times_same_direction == 2):
        turn_1 = (current_direction+1)%4
        turn_2 = (current_direction-1)%4
        for (i,j),direction in [(dir_move[turn_1],turn_1),(dir_move[turn_2],turn_2)]:
            nx,ny = x+i,y+j
            if(not (0 <= nx < len(grid[0]) and 0 <= ny < len(grid))):
                continue
            to_return_nbours.append((heat_value + heat_values[ny][nx],nx,ny,direction,0))
    else:
        for i,j,direction in nbours:
            if(direction == (current_direction+2)%4):
                continue
            nx,ny = x+i,y+j
            if(not (0 <= nx < len(grid[0]) and 0 <= ny < len(grid))):
                continue
            to_return_nbours.append((heat_value + heat_values[ny][nx],nx,ny,direction, num_times_same_direction+1 if current_direction == direction else 0))

    return to_return_nbours


queue = [(0,0,0,UP,0)]
seen = set()
while(queue):
    heat_value,x,y,direction,ntsd = heapq.heappop(queue)
    ident = (x,y,direction,ntsd)
    
    if(ident in seen):
        continue
    else:
        seen.add(ident)
        other_direction = (direction+2)%4
    
    if(grid[y][x] > heat_value):
        grid[y][x] =heat_value
    
    for nbour in get_nbours(x,y,direction,ntsd,heat_value):
        heapq.heappush(queue, nbour)
        


print(grid[-1][-1])
t2 = perf_counter()


print(f"Time : {(t2-t1)*1000:.2f}ms")