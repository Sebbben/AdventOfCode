with open("1.txt") as f:
    cont = f.read()

print(cont.count("(") - cont.count(")"))
