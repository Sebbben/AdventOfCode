with open("2-test.txt", "r") as f:
    reports = list(map(lambda x: list(map(int, x.split(" "))), f.read().splitlines()))

def testReport(report):
    
    asc = [1<=report[i]-report[i-1]<=3 for i in range(1,len(report))]
    desc= [1<=report[i-1]-report[i]<=3 for i in range(1,len(report))]
    
    if all(asc) or all(desc): return True

    if sum(asc) < sum(desc):
        return desc.index(False)
    else:
        return asc.index(False)


tot = 0
for report in reports:
    for i in range(len(report)):
        res = testReport(report[:i]+report[i+1:])
        if type(res) == bool:
            tot += 1
            break
    
print(tot)