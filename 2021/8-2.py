with open("8.txt") as f:
    cont = f.read().splitlines()

tot = 0

for i in cont:
    i = i.split(" | ")
    uniqueSegPatterns = i[0].split(" ")
    outValues = i[1].split(" ")

    uniqueSegPatternsLengths = [len(x) for x in uniqueSegPatterns]

    num1 = set(uniqueSegPatterns[uniqueSegPatternsLengths.index(2)])
    num7 = set(uniqueSegPatterns[uniqueSegPatternsLengths.index(3)])
    num4 = set(uniqueSegPatterns[uniqueSegPatternsLengths.index(4)])
    num8 = set(uniqueSegPatterns[uniqueSegPatternsLengths.index(7)])
    
    fiveSegNums = [x for x in uniqueSegPatterns if len(x)==5]
    middleSeg = list(set(fiveSegNums[0])&set(fiveSegNums[1])&set(fiveSegNums[2])&num4)

    sixSegNums = [x for x in uniqueSegPatterns if len(x)==6]
    for num in sixSegNums:
        if len(set(num)&num1) == 1:
            num6 = set(num)
        elif num.count(middleSeg[0])==1:
            num9 = set(num)
        else:
            num0 = set(num)

    for num in fiveSegNums:
        if len(set(num)^num1)==3:
            num3 = set(num)
        elif len(set(num)^num6)==1:
            num5 = set(num)
        else:
            num2 = set(num)

    nums = {str(sorted(num1)):1,str(sorted(num2)):2,str(sorted(num3)):3,str(sorted(num4)):4,str(sorted(num5)):5,str(sorted(num6)):6,str(sorted(num7)):7,str(sorted(num8)):8,str(sorted(num9)):9,str(sorted(num0)):0}


    out = ""
    for num in outValues:
        out+=str(nums[str(sorted(num))])

    tot += int(out)

print(tot)