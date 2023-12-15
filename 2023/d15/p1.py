from time import perf_counter

t1 = perf_counter()

lines = None
with open("input.txt", "r") as fp:
    lines = fp.read()

parsed = lines.split(",")

total_val = 0
for hash in parsed:
    val = 0
    for i in hash:
        val += ord(i)
        val *= 17
    total_val += val%256

print(total_val)

t2 = perf_counter()

print(f"Time : {(t2-t1)*1000:.2f}ms")