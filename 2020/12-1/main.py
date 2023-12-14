from input_loader import input_loader as il

inp = il.get_input_as_list("input.txt")
#inp = il.get_input_as_list("test.txt")


def main(inp):
    dr = 90
    x = 0
    y = 0

    for i in inp:
        dr = dr % 360
        inst = i[0]
        num = int(i[1:])
        if inst == "F":
            if dr == 0:
                inst = "N"
            elif dr == 90:
                inst = "E"
            elif dr == 180:
                inst = "S"
            elif dr == 270:
                inst = "W"
        if inst == "N":
            x += num
        elif inst == "S":
            x -= num
        elif inst == "E":
            y += num
        elif inst == "W":
            y -= num
        elif inst == "R":
            dr += num
        elif inst == "L":
            dr -= num
    return abs(x) + abs(y)


print(main(inp))
