with open("1.txt") as f:
    data = f.read().splitlines()

list1 = []
list2 = []

for line in data:
    n1,n2 = map(int, line.split("   "))
    list1.append(n1)
    list2.append(n2)

list1 = sorted(list1)
list2 = sorted(list2)

tot = 0
for i in range(len(list1)):
    tot += abs(list1[i]-list2[i])

print(tot)