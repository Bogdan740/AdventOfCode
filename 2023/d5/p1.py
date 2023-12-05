lines = []
with open("input.txt", "r") as fp:
    lines = fp.read().split("\n\n")

seeds = [int(i) for i in lines[0][7:].split()]
maps = lines[1:]

parsed = {}
for i in maps:
    identifier, ranges = i.split(":\n")
    source,_,dest = identifier[:-4].split("-")
    ranges = [[int(j) for j in i.split()] for i in ranges.split("\n")]
    parsed[source] = (dest, ranges)

min_val = float("inf")
for seed in seeds:
    value = seed
    cur_type = "seed"
    while(cur_type!="location"):
        dest, ranges = parsed[cur_type]
        for dest_start,source_start,length in ranges:
            if(source_start <= value < source_start+length):
                value = dest_start+(value-source_start)
                break
        cur_type = dest
    if(value < min_val):
        min_val = value

print(min_val)