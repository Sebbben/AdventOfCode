import re

with open("inp.txt", "r") as f:
    data = f.read().splitlines()
    
# data = """two1nine
# eightwothree
# abcone2threexyz
# xtwone3four
# 4nineeightseven2
# zoneight234
# 7pqrstsixteen""".splitlines()

tot = 0

lookup = ["zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]
 
for line in data:
    
    res = re.findall("(?=(\d|one|two|three|four|five|six|seven|eight|nine))", line)
    num = res[0] if res[0].isnumeric() else str(lookup.index(res[0]))
    num += res[-1] if res[-1].isnumeric() else str(lookup.index(res[-1]))
    tot += int(num)
    # print(num,tot,res,line)
    
print(tot)