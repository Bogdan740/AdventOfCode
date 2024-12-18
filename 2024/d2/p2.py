from time import perf_counter

with open("input.txt", "r") as f:
    lines = f.read().split("\n")


start = perf_counter()

#  Solution

def report_is_safe(report):
    diff = [i-j for (i,j) in zip(report[1:], report[:-1])]
    report_is_safe = all(1<= i <= 3 for i in diff) or all(-1 >= i >= -3 for i in diff)
    return report_is_safe    
parsed_lines = [[int(j) for j in i.split(" ")] for i in lines]
num_safe_reports = 0
for report in parsed_lines:
    for i in range(len(report)):
        if(report_is_safe(report[:i] + report[i+1:])):
            num_safe_reports+=1
            break
            
    
    
# Output
print(num_safe_reports)
end = perf_counter()

# Solution output goes here
print(f"Time: {(end-start) * 1000:.2f}ms")

# Best time 
# 3.88ms