from time import perf_counter

with open("input.txt", "r") as f:
    lines = f.read().split("\n")
    
start = perf_counter()

#  Solution
left = sorted([int(i.split("   ")[0]) for i in lines])
right = sorted([int(i.split("   ")[1]) for i in lines])

end = perf_counter()

# Output
print(sum(abs(i-j) for (i,j) in zip(left, right)))
print(f"Time: {(end-start) * 1000:.2f}ms")

# Best time
# 0.31ms