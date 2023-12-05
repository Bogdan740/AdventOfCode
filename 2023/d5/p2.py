lines = []
with open("input.txt", "r") as fp:
    lines = fp.read().split("\n\n")

seeds = [int(i) for i in lines[0][7:].split()]
maps = lines[1:]

parsed = {}
for i in maps:
    identifier, ranges = i.split(":\n")
    source,_,dest = identifier[:-4].split("-")
    ranges = sorted([[int(j)  for j in i.split()] for i in ranges.split("\n")], key=lambda x:x[1])
    parsed[source] = (dest, ranges)

min_seed_val = float("inf")

for a in range(0,len(seeds),2):
    i,j = seeds[a],seeds[a+1]
    seed = i
    while seed < i+j:
        # print(100*(seed-i)/j)
        seed_val = seed
        cur_type = "seed"
        least_distance_to_next_interest = float("inf")
        advance_by = float("inf")
        while(cur_type!="location"):
            dest, ranges = parsed[cur_type]
            for d_start, s_start, width in ranges:
                distance_to_next = s_start+width-seed_val
                distance_to_start = s_start - seed_val
                if(distance_to_next > 0 and distance_to_next < advance_by):
                    advance_by=distance_to_next
                if(distance_to_start > 0 and distance_to_start < advance_by):
                    advance_by=distance_to_start
                    
                if(s_start <= seed_val < s_start+width):
                    seed_val = d_start+(seed_val - s_start)
                    break
            cur_type = dest
        seed+=advance_by if advance_by != 0 and advance_by != float("inf") else 1
        if(seed_val < min_seed_val):
            min_seed_val = seed_val
    
print(min_seed_val)

#780711947

#4283162641