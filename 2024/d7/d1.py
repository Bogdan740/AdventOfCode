from time import perf_counter

with open("input.txt", "r") as f:
    lines = f.read().split("\n")
    
start = perf_counter()

def solve(target, nums):
    if(len(nums) == 1):
        return target == nums[0]
    fst, *rest = nums
    to_return = solve(target/fst, rest) or solve(target-fst, rest)
    return to_return
        
#  Solution
parsed = [(int(i.split(": ")[0]),[int(j) for j in i.split(": ")[1].split()]) for i in lines]
total_calibration_results = 0
for target, nums in parsed:
    if(solve(target, nums[::-1])):
        total_calibration_results += target
        
# Output
print(total_calibration_results)
end = perf_counter()

# Solution output goes here
print(f"Time: {(end-start) * 1000:.2f}ms")

# Best time
# 37.15ms