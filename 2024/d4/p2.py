from time import perf_counter

with open("input.txt", "r") as f:
    lines = f.read().split("\n")
    
start = perf_counter()

#  Solution

total = 0
inner_range = [k for k in range(len(lines)) if 1 <= k < len(lines)-1]
for i in inner_range:
    for j in inner_range:
        center = lines[i][j]
        if(center != "A"):
            continue
        tl = lines[i-1][j-1]
        tr = lines[i-1][j+1]
        br = lines[i+1][j+1]
        bl = lines[i+1][j-1]
        diag = bl+center+tr
        antidiag = tl+center+br
        if((diag.count("MAS") or diag[::-1].count("MAS")) and (antidiag.count("MAS") or antidiag[::-1].count("MAS"))):
            total+=1


# Output
end = perf_counter()
print(total)
print(f"Time: {(end-start) * 1000:.2f}ms")

# Best time
# 3.01ms