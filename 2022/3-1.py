with open("3.txt") as f:
    cont = f.read().splitlines()

tot = 0
for i in cont:
    similar = (set(i[:len(i)//2]) & set(i[len(i)//2:])).pop()
    if similar.upper() == similar:
        tot += ord(similar)-ord("A") + 27
        print(similar, ord(similar)-ord("A") + 27)
    else:
        tot += ord(similar)-ord("a") + 1
        print(similar, ord(similar)-ord("a") + 1)

    # print(similar, ord(similar)-ord("A"))

print(tot)