from time import perf_counter

t1 = perf_counter()

patterns = []

with open("input.txt", "r") as fp:
    patterns = fp.read().split("\n\n")

patterns_as_rows = [pattern.split("\n") for pattern in patterns]
patterns_as_cols = [["".join(reversed([pattern[i][j] for i in range(len(pattern))])) for j in range(len(pattern[0])) ] for pattern in patterns_as_rows]

def find_reflection_val(rows, cols, original = None):
    for split in range(1,len(rows)):
        # This check saves a lot of time
        if(rows[split-1] != rows[split]):
            continue
        
        split1 = rows[:split]
        split2 = rows[split:]
        
        shortest_dist = min(len(split1), len(split2))
        split1 = "".join(split1[-shortest_dist:])
        split2 = "".join(split2[:shortest_dist][::-1])
        
        if(split1 == split2 and 100*split != original):
            return(100*split)
        

    for split in range(1,len(cols)):
        # This check saves a lot of time
        if(cols[split-1] != cols[split]):
            continue
        split1 = cols[:split]
        split2 = cols[split:]

        
        shortest_dist = min(len(split1), len(split2))
        
        split1 = "".join(split1[-shortest_dist:])
        split2 = "".join(split2[:shortest_dist][::-1])
        
        if(split1 == split2 and split!=original):
            return(split)
    
    return -1

def find_diff_reflection(rows, cols, original_ref_val):
    for x in range(len(rows)):
        for y in range(len(cols)):
            new_rows = [row if i != x else row[:y] + ("#" if row[y] == "." else ".")+row[y+1:] for i,row in enumerate(rows)]
            new_cols = [col if i != y else col[:x] + ("#" if col[x] == "." else ".")+col[x+1:] for i,col in enumerate(cols)]
            new_ref_val = find_reflection_val(new_rows, new_cols, original_ref_val)
            if(new_ref_val != -1 ):
                return new_ref_val

total = 0
for rows,cols in zip(patterns_as_rows, patterns_as_cols):
    original_ref_val = find_reflection_val(rows, cols)
    diff_reflection = find_diff_reflection(rows,cols, original_ref_val)
    total += diff_reflection
    
    
print(total)
t2 = perf_counter()

print(f"Time : {(t2-t1)*1000:.2f}ms")

# 28762 - TOO LOW