from time import perf_counter

with open("input.txt", "r") as f:
    lines = f.read().split("\n")
    
start = perf_counter()

def solve(target, nums):
    if(target == ""):
        return False
    target = float(target)
    if(len(nums) == 1):
        return target == nums[0]
    fst, *rest = nums
    to_return = solve(str(target/fst), rest) or solve(str(target-fst), rest)
    target_ends_with_fst = target >= 0 and target%1 == 0 and str(int(target)).endswith(str(fst))
    to_return = to_return or (target_ends_with_fst and solve(str(int(target))[:-len(str(fst))], rest))
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
# 240.15ms