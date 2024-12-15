from time import perf_counter

with open("input.txt", "r") as f:
    lines = f.read().split("\n")
    
#  Solution
start = perf_counter()
left = sorted([int(i.split("   ")[0]) for i in lines])
right = sorted([int(i.split("   ")[1]) for i in lines])

end = perf_counter()

# Output
print(sum(i * right.count(i) for i in left))
print(f"Time: {(end-start) * 1000:.2f}ms")

# Best time
# 0.31ms