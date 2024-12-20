from time import perf_counter

with open("input.txt", "r") as f:
    lines = f.read().split("\n")


start = perf_counter()

#  Solution

parsed_lines = [[int(j) for j in i.split(" ")] for i in lines]
num_safe_reports = 0
for report in parsed_lines:
    diff = [i-j for (i,j) in zip(report[1:], report[:-1])]
    report_is_safe = all(1<= i <= 3 for i in diff) or all(-1 >= i >= -3 for i in diff)
    num_safe_reports += report_is_safe
    
# Output
print(num_safe_reports)
end = perf_counter()

# Solution output goes here
print(f"Time: {(end-start) * 1000:.2f}ms")

# Best time 
# 1.10ms