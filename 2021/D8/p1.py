f = open("puzzleinput.txt", "r")
testData = f.read()
f.close()

# inputArr = list(map(int, testData.split(",")))

# First I want to see if I can identify 2 displays uniquely by their differences
segments = ["abcefg", "cf", "acdeg", "acdfg", "bcdf",
            "abdfg", "cefg", "acf", "abcdefg", "abcdfg"]

count = sum(1 for a, b in zip("abc", "abcde") if a == b)
print(count)
