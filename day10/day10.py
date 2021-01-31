
def calculate_longest_path(input):
    difference_1 = 0
    difference_2 = 0
    difference_3 = 0
    for pointer in range(-1,len(input)):
        if pointer == -1:
            curr = 0
        else:
            curr = input[pointer]
        if pointer + 1 < len(input):
            next = input[pointer+1]
            diff = next - curr
            print(curr, diff)
            if diff == 1:
                difference_1 +=1
            elif diff == 2:
                difference_2 += 1
            else:
                difference_3 +=1
        else:
            difference_3+=1
    print(difference_1, difference_2, difference_3, difference_1* difference_3)

def explode_combos(lines):
    count = 0
    index = 1

    possible_combos = []
    #for i



def count_valid_path(input):

    valid_combos = {}
    for adap in input:
        for adap2 in input:
            if adap2 - 3 <= adap and adap2 > adap:
                if adap not in valid_combos:
                    valid_combos[adap] = []
                valid_combos[adap].append(adap2)
    valid_paths = 1
    print(valid_combos)

    #for item in input:


    # for key, vc in valid_combos.items():
    #     if len(vc) == 3  and valid_paths == 1:
    #         valid_paths = 4
    #     elif len(vc) == 2:
    #         valid_paths += 2
    #     elif len(vc) == 3:
    #         valid_paths += 3
    #     print(key,  vc)

def build_map(input):
    map = {}
    counter = 1
    for i in input:
        map[i]  = []
        for distance in range(0,3):
            if counter+distance < len(input) and input[counter + distance] <= i+3:
                map[i].append(input[counter+distance])
        counter+=1
    return map

#print(explode_combos([4,5,6,7]))
def find_flex_points(input, map):
    flex_points = []
    i = 0
    while i < len(input):
        start_flex = i
        end_flex = -1
        while i < len(input) and not (len(map[input[i]]) == 1 and len(map[map[input[i]][0]]) >1):
            end_flex = i
            i+=1
        i+=1

        if i > len(input):
            end_flex = len(input)-1
        else:
            end_flex=i
        if end_flex >= 0:
            flex_points.append([start_flex, end_flex])

    return flex_points

def flex_point_variation(input, map, start_index, stop_index):
    possible_options = []
    counter = 1
    if start_index == stop_index:
        return 2
    counter = 4
    for i in range(start_index, stop_index):
        if len(map[input[i]]) == 3:
            counter= counter+2
        # elif len(map[input[i]]) == 2 and i != stop_index:
        #     print('yo')
        #     counter = counter*3
    return counter

def flex_point_variation2(input, start_index, stop_index, depth = 1):
    possible = []
    if start_index == stop_index:
        return [[input[stop_index]]]
    for i in range(0,depth):
        mod = 0
        for sub_list in flex_point_variation2(input, start_index+1, stop_index, depth+1):
            list = []
            if mod % 2 == 0:
                list = [input[start_index]]
            list.extend(sub_list)
            mod+=1
            possible.append(list)
    return possible

def all_combos(list):
    combos = []
    counter = 0
    bit = 0
    for counter in range(0, len(list)):
        combos.append(set())
        for i in list:
            combos[counter].add(i)
            for j in list[1:]:
                if bit %2 ==0:
                    combos[counter].add(j)
                bit+=1

    print(combos)

def use_map(map, root, stop_val):
    count = 0
    routes = []
    if root == stop_val:
        return 1
    if len(map[root]) == 0:
        return 1#, [[root]]
    else:
        for valid in map[root]:
            cnt = use_map(map, valid, stop_val)
            count += cnt
            # for rt in rts:
            #     rt.insert(0, root)
            #     routes.append(rt)

    return count#, routes

#all_combos([1,2,3,4,5])

with open('input.txt') as f:
    input = []
    for line in f:
        input.append(int(line.strip()))

    input.sort()
    input.insert(0,0)
    map = build_map(input)
    flex_points = find_flex_points(input, map)
    results = 1
    print(input)
    # count = use_map(map,input[0])
    count = 1
    for f_start, f_stop in flex_points:
        print(input[f_start:f_stop])
        count *= use_map(map, input[f_start], input[f_stop])
        print(count)
    #     results *= count
    #     print(points)
    print(count)
    # print (results)

    valid_paths = 1
    for flex_point in flex_points:

        # fpv = flex_point_variation(input, map, flex_point[0], flex_point[1])
        possible = flex_point_variation2(input, flex_point[0], flex_point[1]+2)
        # for p in possible:
        #     print(p)

        # print(flex_point, fpv)
        # valid_paths = valid_paths * fpv
    # print(valid_paths)
    # count_valid_path(input)



