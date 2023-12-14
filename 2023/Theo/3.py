def ajecent(line, indexes):
    not_symbols = list('0123456789.')
    is_ajecent = False

    for i in indexes:
        if line[i] not in not_symbols:
            is_ajecent = True
    
    if not is_ajecent:
        is_ajecent = (indexes[0] != 0 and line[indexes[0]-1] not in not_symbols) or (indexes[-1] != len(line)-1 and line[::-1][len(line) - indexes[-1] - 2] not in not_symbols)
        
    return is_ajecent


def part_numbers(previous_line=False, line=None, next_line=False):
    not_symbols = list('0123456789.')

    numbers = list()
    number_now = False

    number = str()
    indexes = list()
    for i in range(len(line)):
        if line[i] in not_symbols[:-1]:
            number_now = True

            number += line[i]
            indexes.append(i)
            is_part_number = False
        elif number_now:
            number_now = False

            if not is_part_number:
                is_part_number = (indexes[0] != 0 and line[indexes[0]-1] not in not_symbols) or (indexes[-1] != len(line)-1 and line[::-1][len(line) - indexes[-1] - 2] not in not_symbols)
            if previous_line and not is_part_number:
                is_part_number = ajecent(previous_line, indexes=indexes)
            if next_line and not is_part_number:
                is_part_number = ajecent(next_line, indexes=indexes)
            
            if is_part_number:
                numbers.append(int(number))

            number = str()
            indexes = list()

    return numbers           


with open('inp.txt', 'r') as file:
    lines = file.readlines()
    data_nums = list()

    for i in range(len(lines)):
        if i == 0:
            data_nums.append(part_numbers(line=lines[i], next_line=lines[i+1]))
        elif i == len(lines) - 1:
            data_nums.append(part_numbers(previous_line=lines[i-1], line=lines[i]))
        else:
            data_nums.append(part_numbers(previous_line=lines[i-1], line=lines[i], next_line=lines[i+1]))
    
    # Dette er bare for å sjekke
    for i, nums in enumerate(data_nums):
        print(i+1, len(nums))
    sum = 0
    for line_nums in data_nums:
        for nums in line_nums:
            sum += nums
    
    print(sum)
