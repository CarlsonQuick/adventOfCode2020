import numpy

with open('input.txt') as f:
    hill = [[digit for digit in line.strip()] for line in f]



def check_hill(x_step, y_step, hill):
    height = len(hill)
    width = len(hill[0]) - 1
    x_pos = 0
    hit_tree =0
    for y_pos in range(y_step,height,y_step):
        if x_pos + x_step <= width:
            x_pos += x_step
        else:
            x_pos = x_pos + x_step - 1  - width
        if hill[y_pos][x_pos] == '#':
            hit_tree +=1
            # hill[y_pos][x_pos] = 'X'
    #     else:
    #         hill[y_pos][x_pos] = 'O'
    #
    # for h in hill:
    #     print(h)
    return hit_tree

step_options = [(1,1), (3,1), (5,1), (7,1), (1,2)]
total = 1
for option in step_options:
    hit_tree = check_hill(option[0], option[1], hill)
    total = total*hit_tree
    print(hit_tree)


print(total)

