import math

def midpoint(lower, upper, go_up):
    if go_up:
        return math.ceil(lower + (upper - lower) / 2), upper
    else:
        return lower, upper - int(( upper - lower) / 2)-1


code_max = 0

with open('input.txt') as f:
    #FBFBBFFRLR
    seating_chart = {}
    ids = []
    for code in f:
        code = code.strip()
        min = 0
        max = 127
        for row_dir in code[0:7]:
            min, max = midpoint(min, max, row_dir == 'B')
            print(min, max)

        c_min = 0
        c_max = 7
        for seat_dir in code[7:10]:
            c_min, c_max = midpoint(c_min, c_max, seat_dir == 'R')


        if row_dir == 'F':
            row_val = min
        else:
            row_val = max
        if seat_dir == 'L':
            col_val = c_min
        else:
            col_val = c_max

        if row_val not in seating_chart:
            seating_chart[row_val] = set()

        seating_chart[row_val].add(col_val)
        seat_id = row_val*8 + col_val
        if seat_id > code_max:
            code_max = seat_id
        ids.append(seat_id)
        print('row: ', row_val, 'seat: ', col_val, ' code: ', seat_id)

#print(code_max)
ids.sort()
prev = 0
for i in ids:
    if prev+1 != i:
        print(i)
    prev = i
# seats = range(0,7)
# for r in range(1,127):
#      if r in seating_chart:
#          print(r, seating_chart[r])
# for row in seating_chart:
#     for seat in seats:
#         if seat not in seating_chart[row]:
#             print(min * 8 + c_min)

