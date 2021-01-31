
rnge = 25

def sum_matches(list, value):
    for a in list:
        for b in list[1:len(list)]:
            if a+b == value:
                return True
    return False

def find_weakness(list, target, start_point):
    sum = 0
    smallest = 498507365515190
    largest =  0
    index = start_point
    while sum < target and index < len(list):
        sum += list[index]
        if smallest > list[index]:
            smallest = list[index]
        if largest < list[index]:
            largest = list[index]
        index+=1

    if sum == target:
        return True, smallest, largest
    return False, smallest, largest


with open('input.txt') as f:
    input = []
    for line in f:
        input.append(int(line.strip()))

    target = 0
    frame_start = 0
    frame_end = rnge
    for number in input[rnge:len(input)]:
        if not sum_matches(input[frame_start:frame_end], number):
            target = number
        frame_start +=1
        frame_end +=1

    for start_index in range(0,len(input)):

        found, smallest, largest = find_weakness(list=input, target=target, start_point= start_index)
        if found:
            print(found, smallest, largest, smallest+largest)

