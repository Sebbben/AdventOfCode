with open("2.txt", "r") as f:
    reports = list(map(lambda x: list(map(int, x.split(" "))), f.read().splitlines()))

print(sum([
    all(
        1<=report[i]-report[i-1]<=3 for i in range(1,len(report))
    ) or 
    all(
        1<=report[i-1]-report[i]<=3 for i in range(1,len(report))
    )
    for report in reports
]))