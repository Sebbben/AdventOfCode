from input_loader import input_loader as il

inp = il.get_input_as_list("input.txt")
#inp = il.get_input_as_list("test.txt")


def main(inp):
    mem = {}
    mask = "X"*36
    for line in inp:
        if line.startswith("mask"):
            mask = line.split(" ")[-1][::-1]
            print(mask)
            
        else:
            tmp = line.split(" ")
            index = tmp[0].split("[")[-1][:-1]
            val = tmp[-1]
            
            newNum = ""
            val = str(bin(int(val)))[2:][::-1]
            
            for i in range(len(val)):
                if mask[i] == "X":
                    newNum += val[i]
                else:
                    newNum += mask[i]
                    
            for i in mask[len(val):]:
                if i == "X":
                    newNum += "0"
                else:
                    newNum += i
            newNum = newNum[::-1]
            print(int(newNum,2))
            mem[index] = int(newNum,2)
    return sum(mem.values())
print(main(inp))
