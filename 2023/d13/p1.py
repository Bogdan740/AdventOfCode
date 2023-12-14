from time import perf_counter

t1 = perf_counter()

patterns = []

with open("input.txt", "r") as fp:
    patterns = fp.read().split("\n\n")

patterns_as_rows = [pattern.split("\n") for pattern in patterns]
patterns_as_cols = [["".join(reversed([pattern[i][j] for i in range(len(pattern))])) for j in range(len(pattern[0])) ] for pattern in patterns_as_rows]

total = 0

for rows,cols in zip(patterns_as_rows, patterns_as_cols):
    for split in range(1,len(rows)):
        # This check saves a lot of time
        if(rows[split-1] != rows[split]):
            continue
        split1 = rows[:split]
        split2 = rows[split:]

        shortest_dist = min(len(split1), len(split2))
        split1 = "".join(split1[-shortest_dist:])
        split2 = "".join(split2[:shortest_dist][::-1])
        
        if(split1 == split2):
            total+=(100*split)
            break
        
    
    for split in range(1,len(cols)):
        # This check saves a lot of time
        if(cols[split-1] != cols[split]):
            continue
        split1 = cols[:split]
        split2 = cols[split:]

        shortest_dist = min(len(split1), len(split2))
        split1 = "".join(split1[-shortest_dist:])
        split2 = "".join(split2[:shortest_dist][::-1])
        
        if(split1 == split2):
            total+=split
            break


print(total)

t2 = perf_counter()

print(f"Time : {(t2-t1)*1000:.2f}ms")
# 30535 - TOO LOW