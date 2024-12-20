from time import perf_counter
import re

with open("input.txt", "r") as f:
    line = f.read()
    
start = perf_counter()
#  Solution

valid_instructions = re.findall("mul\\([0-9][0-9]?[0-9]?,[0-9][0-9]?[0-9]?\\)", line)
mult_pairs = [i[4:-1].split(",") for i in valid_instructions]
answer = 0
for i,j in mult_pairs:
    answer += int(i)*int(j)
# Output
print(answer)
end = perf_counter()

# Solution output goes here
print(f"Time: {(end-start) * 1000:.2f}ms")

# Best time
# 0.30ms