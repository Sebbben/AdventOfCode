from input_loader import input_loader as il

inp = il.get_input_as_list("input.txt")
#inp = il.get_input_as_list("test.txt")


def main(inp):
    x = 0
    y = 0

    waypoint = [1, 10]

    for i in inp:
        inst = i[0]
        num = int(i[1:])
        if inst == "F":
            x += num*waypoint[0]
            y += num*waypoint[1]
        if inst == "N":
            waypoint[0] += num
        elif inst == "S":
            waypoint[0] -= num
        elif inst == "E":
            waypoint[1] += num
        elif inst == "W":
            waypoint[1] -= num
        elif inst == "L":
            if num == 90:
                waypoint = [waypoint[1], -waypoint[0]]
            elif num == 180:
                waypoint = [-waypoint[0], -waypoint[1]]
            elif num == 270:
                waypoint = [-waypoint[1], waypoint[0]]
        elif inst == "R":
            if num == 90:
                waypoint = [-waypoint[1], waypoint[0]]
            elif num == 180:
                waypoint = [-waypoint[0], -waypoint[1]]
            elif num == 270:
                waypoint = [waypoint[1], -waypoint[0]]

        print(x, y, i, waypoint)
    return abs(x) + abs(y)


print(main(inp))
