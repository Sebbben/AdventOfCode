from collections import Counter
from collections import defaultdict

with open("1.txt") as f:
    data = f.read().splitlines()

list1 = []
list2 = []

for line in data:
    n1,n2 = map(int, line.split("   "))
    list1.append(n1)
    list2.append(n2)

numsL2 = defaultdict(lambda: 0, Counter(list2))

tot = 0
for num in list1:
    tot += num * numsL2[num]

print(tot)
    