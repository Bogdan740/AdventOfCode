from time import perf_counter

t1 = perf_counter()

lines = None
with open("input.txt", "r") as fp:
    lines = fp.read()

parsed = [(line.split("-"),"-") if "-" in line else (line.split("="),"=") for line in lines.split(",")]

def HASH(hash):
    val = 0
    for i in hash:
        val += ord(i)
        val *= 17
    return val%256

boxes = {}
for ((label, foc), op) in parsed:
    box = HASH(label)
    if(op == "-"):
        if(box not in boxes):
            continue

        box_contents = boxes[box]
        for i,(lense_label, lense_focal) in enumerate(box_contents):
            if(lense_label == label):
                boxes[box].pop(i)
                break
    else:
        if(box not in boxes):
            boxes[box] = []
        
        box_contents = boxes[box]
        insert_index = 0
        for i,(lense_label, lense_focal) in enumerate(box_contents):
            if(lense_label == label):
                boxes[box].pop(i)
                insert_index = i
                break
        boxes[box].insert(insert_index, (label, int(foc)))

total_focusing_power = 0
for i in boxes:
    contents = boxes[i]
    focusing_power = 0
    for j,(label,foc) in enumerate(contents):
        focusing_power += (1+i)*(len(contents)-j)*(foc)
    total_focusing_power+=focusing_power

print(total_focusing_power)

t2 = perf_counter()

print(f"Time : {(t2-t1)*1000:.2f}ms")