from time import perf_counter

with open("input.txt", "r") as f:
    lines = f.read().split("\n")
    
start = perf_counter()

chars = {}
#  Solution

def is_inbounds(coords):
    x,y = coords
    return 0 <= x < len(lines) and 0 <= y < len(lines[0])
    
for i in range(len(lines)):
    for j in range(len(lines[i])):
        char = lines[i][j]
        if(char != "."):
            if(char not in chars):
                chars[char] = [(i,j)]
            else:
                chars[char].append((i,j))

antinodes = set()            
for char in chars:
    coords = chars[char]
    for i in range(len(coords)):
        for j in range(i+1,len(coords)):
            x1,y1 = coords[i]
            x2,y2 = coords[j]
            dx,dy = x1-x2, y1-y2
            antinode1 = (x1+dx,y1+dy)
            antinode2 = (x2-dx,y2-dy)
            if(is_inbounds(antinode1)):
                antinodes.add(antinode1)
            if(is_inbounds(antinode2)):
                antinodes.add(antinode2)                
            
# Output
print(len(antinodes))
end = perf_counter()

# Solution output goes here
print(f"Time: {(end-start) * 1000:.2f}ms")

# Best time
# 0.39ms