from time import perf_counter
import re

with open("input.txt", "r") as f:
    line = f.read()
    
start = perf_counter()
#  Solution

all_instructions = re.findall(r"mul\([0-9][0-9]?[0-9]?,[0-9][0-9]?[0-9]?\)|don't\(\)|do\(\)", line)

do = True
total = 0
for ins in all_instructions:
    match ins:
        case "do()":
            do = True
        case "don't()":
            do = False
        case mult_instruction:
            if(do):
                a,b = list(map(int,mult_instruction[4:-1].split(",")))
                total += a*b

# Output
print(total)
end = perf_counter()

# Solution output goes here
print(f"Time: {(end-start) * 1000:.2f}ms")

# Best time
# 0.39ms