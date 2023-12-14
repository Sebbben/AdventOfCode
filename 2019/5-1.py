with open("5.txt") as f:
    cont = f.read().split(",")

i = 0
while cont[i] != 99:
    method = str(cont[i])
    method = "0"*(5-len(method)) + method
    if method[-2:] == "01":
        par1 = int(cont[i+1]) if method[-3] == "1" else int(cont[int(cont[i+1])])
        par2 = int(cont[i+2]) if method[-4] == "1" else int(cont[int(cont[i+2])])
        if method[-5] == "0":
            cont[int(cont[int(cont[i+3])])] = par1+par2
        else:
            cont[int(cont[i+3])] = par1+par2

        i += 4
    elif method[-2:] == "02":
        par1 = int(cont[i+1]) if method[-3] == "1" else int(cont[int(cont[i+1])])
        par2 = int(cont[i+2]) if method[-4] == "1" else int(cont[int(cont[i+2])])
        if method[-5] == "0":
            cont[int(cont[int(cont[i+3])])] = par1*par2
        else:
            cont[int(cont[i+3])] = par1*par2
        i += 4
    elif method[-2:] == "03":
        num = int(input("Enter input\n>"))
        cont[int(cont[i+1])] = num
        input(f"set {cont[i+1]} to {num}")
        i += 2
    elif method[-2:] == "04":
        print("Program output:",cont[int(cont[i+1])])
        i += 2
    else:
        input(method + "rnkoorem")