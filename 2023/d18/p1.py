from time import perf_counter

t1 = perf_counter()

lines = []
with open("input.txt", "r") as fp:
    lines = fp.read().split("\n")

parsed = [(line.split(" ")[0],int(line.split(" ")[1]),line.split(" ")[2][2:-1]) for line in lines]

vertices = [(0,0)]
x,y = 0,0
perim = 0
directions = {"R" : (1,0), "L" : (-1,0), "U" : (0,-1), "D" : (0,1)}
for (direction, length, _) in parsed:
    dx,dy = directions[direction]
    x+= length * dx
    y+= length * dy
    perim+=length

    vertices.append((x,y))

total = sum(x1*y2-x2*y1 for (x1,y1),(x2,y2) in zip(vertices, vertices[1:]))
area = 1/2* abs(total)
interior = area - (perim/2)+1
print(int(interior + perim))

t2 = perf_counter()

print(f"Time : {(t2-t1)*1000:.2f}ms")