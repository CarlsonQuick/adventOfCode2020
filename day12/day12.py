

def get_instructions():
    instructions = []
    with open('input.txt') as f:
        for line in f:
            line = line.strip()
            inst = line[0]
            size = int(line[1:])
            instructions.append((inst,size))
    return instructions

def rotate(facing, direction, magnitude):
    cardinal_points = ['N','E','S','W']
    turns = int(magnitude / 90)
    if direction == 'L':
        turns = turns * -1
    curr_pos = cardinal_points.index(facing)
    new_pos = curr_pos + turns
    if new_pos < 0:
        new_pos = new_pos + 4
    if new_pos >= len(cardinal_points):
        new_pos = new_pos - 4
    # print( 'facing', facing, 'turned ', direction, magnitude, 'and ended up facing', cardinal_points[new_pos])
    return cardinal_points[new_pos]
def rotate_waypoint(waypoint, direction, magnitude):
    turns = int(magnitude/90)
    cwp = waypoint
    if direction == 'L':
        turns = 4 - turns
    for i in range(0,turns):
        ns = cwp[0]
        ew = cwp[1]
        if (ns < 0 and ew < 0):
            ew = cwp[0]
            ns = cwp[1] * -1

        elif (ns > 0 and ew > 0):
            ns = cwp[1] * -1
            ew = cwp[0]
        elif( ns > 0 and ew < 0):
            ns  = cwp[1] * -1
            ew = cwp[0]
        else:
            ew = cwp[0]
            ns = cwp[1] * -1
        cwp = [ns,ew]
    return cwp



def __direction(dir):
    if dir == 'N' or dir == 'E':
        return -1
    if dir == 'S' or dir == 'W':
        return 1

def move_forward(curr_pos, length):
    length = length * __direction(curr_pos[2])
    if curr_pos[2] == 'N' or curr_pos[2] == 'S':
        curr_pos[0] += length
    else:
        curr_pos[1] += length
    # print('moved ', length, 'along the ', curr_pos[2], 'axis')
    return curr_pos

def move_to_waypoint(curr_pos,waypoint, length):
    for count in range(0,length):
        curr_pos[0] += waypoint[0]
        curr_pos[1] += waypoint[1]
        # print('moved ', length, 'along the ', curr_pos[2], 'axis')
    return curr_pos

def move(curr_pos, direction,magnitude):
    magnitude = magnitude * __direction(direction)
    if direction == 'N' or direction == 'S':
        curr_pos[0] += magnitude
    else:
        curr_pos[1] += magnitude
    return curr_pos
def move_waypoint(waypoint, direction,magnitude):
    magnitude = magnitude * __direction(direction)
    if direction == 'N' or direction == 'S':
        waypoint[0] += magnitude
    else:
        waypoint[1] += magnitude
    return waypoint

def manhatten_distance(curr_pos, starting_pos):
    ns = abs(curr_pos[0]) + abs(starting_pos[0])
    ew = abs(curr_pos[1]) + abs(starting_pos[1])
    print('ns', ns, 'ew', ew,'sum',ns+ew)
    return ns+ew

inst = get_instructions()
def round2():
    starting_pos = (0,0,'E')
    waypoint = [-1,-10]
    curr_pos = [0,0,'E']
    for i in inst:
        if i[0] == 'L' or i[0] == 'R':
            waypoint = rotate_waypoint(waypoint, i[0], i[1])
        elif i[0] == 'F':
            curr_pos = move_to_waypoint(curr_pos,waypoint,  i[1])
        else:
            waypoint = move_waypoint(waypoint, i[0], i[1])
        print(curr_pos, waypoint)
    print( manhatten_distance( curr_pos,starting_pos))

def round1():
    starting_pos = (0,0,'E')
    curr_pos = [0,0,'E']
    for i in inst:
        if i[0] == 'L' or i[0] == 'R':
            curr_pos[2] = rotate(curr_pos[2], i[0], i[1])
        elif i[0] == 'F':
            curr_pos = move_forward(curr_pos, i[1])
        else:
            curr_pos = move(curr_pos, i[0], i[1])
        print(curr_pos)
    print( manhatten_distance( curr_pos,starting_pos))
round2()
