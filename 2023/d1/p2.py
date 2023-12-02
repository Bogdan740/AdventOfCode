lines = None
with open("input.txt") as fp:
    lines = fp.readlines()

digits_map = {
    "one" : "1",
    "two" : "2",
    "three" : "3",
    "four" : "4",
    "five" : "5",
    "six" : "6",
    "seven" : "7",
    "eight" : "8",
    "nine" : "9",
    
}
s = 0
for line in lines:
    first = None
    last = None
    for i,char in enumerate(line):
        if(char.isdigit()):
            if(first == None):
                first = char
                last = char
            else:
                last = char
        else:
            for k in range(3,6):
                c= line[i:i+k] if i+k < len(line) else "none"
                c_digit = digits_map[c] if c in digits_map else None
                if(c_digit):
                    if(first == None):
                        first = c_digit
                        last = c_digit
                    else:
                        last = c_digit
                    
                
        
    s += int(first+last)

print(s)