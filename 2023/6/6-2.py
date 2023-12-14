with open("inp.txt", "r") as f:
    times, distances = f.read().splitlines()


# times,distances = """Time:      7  15   30
# Distance:  9  40  200""".splitlines()

from math import sqrt, ceil
times = list(map(int, times.split()[1:]))
distances = list(map(int, distances.split()[1:]))

races = list(zip(times, distances))

def f(x,a):
    return (a-x)*x
    # ax-x**2=y
    # -x^2+ax-y=0
    
    # b = (-a+sqrt(a**2+4*y))/-2
    # c = (-a-sqrt(a**2-4*y))/-2
    # return ceil(max(b,c))

tot = 1
for race in races:
    
    winns = 0
    for i in range(race[0]):
        if f(i,race[0]) > race[1]:
            # print(i)
            winns += 1
        
    print(winns)
    tot *= winns
    
    
print(tot)