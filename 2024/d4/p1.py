from time import perf_counter

with open("input.txt", "r") as f:
    lines = f.read().split("\n")
    
start = perf_counter()

#  Solution

def get_diags(c):
    counter_diag_1 = [ row[-(i+c+1)] for i,row in enumerate(lines) if 0 <= i+c < len(row)]
    diag_1 = [ row[i+c] for i,row in enumerate(lines) if 0 <= i+c < len(row)]
    to_return = [
        "".join(counter_diag_1),
        "".join(counter_diag_1[::-1]),
         "".join(diag_1),
        "".join(diag_1[::-1]),
        
    ]
    if(c != 0):
        counter_diag_2 = [ row[-(i-c+1)] for i,row in enumerate(lines) if 0 <= i-c < len(row)]
        diag_2 = [ row[i-c] for i,row in enumerate(lines) if 0 <= i-c < len(row)]
        to_return += [
            "".join(counter_diag_2),
            "".join(counter_diag_2[::-1]),
            "".join(diag_2),
            "".join(diag_2[::-1])
        ]
    
    return to_return

total = 0

# across
for row in lines:
    total+= row.count("XMAS")
    total+= "".join(row[::-1]).count("XMAS")
# down
for column in list(zip(*lines)):
    total += "".join(column).count("XMAS")
    total+= "".join(column[::-1]).count("XMAS")

for c in range(len(lines)):
    for diag in get_diags(c):
        total+= diag.count("XMAS")


# Output
end = perf_counter()
print(total)
print(f"Time: {(end-start) * 1000:.2f}ms")

# Best time
# 4.59ms