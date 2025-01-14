from time import perf_counter

with open("input.txt", "r") as f:
    lines = f.read().split("\n")
    
start = perf_counter()

#  Solution
parsed = lines[0]
new_string = []
is_file_space = True
file_counter = 0
for num in map(int,parsed):
    if(is_file_space):
        new_string = new_string + [str(file_counter)] * num
        file_counter+=1
    else:
        new_string = new_string + ["."] * num
    
    is_file_space = not is_file_space

dot_pointer = 0
file_pointer = len(new_string)-1
while(dot_pointer < file_pointer):
    while(new_string[dot_pointer] != "."):
        dot_pointer+=1
    while(new_string[file_pointer] == "."):
        file_pointer-=1

    if(dot_pointer < file_pointer):
        new_string[dot_pointer] = new_string[file_pointer]
        new_string[file_pointer] = "."

answer = sum([int(val)*i for i,val in enumerate(new_string) if val != "."])
# Output
print(answer)
end = perf_counter()

# Solution output goes here
print(f"Time: {(end-start) * 1000:.2f}ms")

# Best time
# TODO