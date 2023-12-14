with open("3.txt") as f:
    cont = f.read().splitlines()

gammaCont = cont.copy()
epsilonCont = cont.copy()

for bit in range(len(gammaCont[0])):
    pos = [i[bit] for i in gammaCont]
    majority = str(int(pos.count("1") >= pos.count("0")))

    gammaCont = [i for i in gammaCont if i[bit] == majority]

    if len(gammaCont) == 1:
        print(gammaCont[0])
        break

for bit in range(len(epsilonCont[0])):
    pos = [i[bit] for i in epsilonCont]
    majority = str(int(not bool(int(pos.count("1") >= pos.count("0")))))

    epsilonCont = [i for i in epsilonCont if i[bit] == majority]

    if len(epsilonCont) == 1:
        print(epsilonCont[0])
        break

print(int(gammaCont[0],2)*int(epsilonCont[0],2))