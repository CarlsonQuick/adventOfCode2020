import pandas as pd
def get_input():
    with open('input.txt') as f:
        timestamp = int(f.readline().strip())
        busses = f.readline().strip().split(',')
    return timestamp, busses
def build_schedule(ts, bus):
    sched = []
    for tick in range(0,ts+479):
        if tick % bus == 0:
            sched.append('D')
        else:
            sched.append('.')
    return sched
def round1():
    ts, busses = get_input()
    bus_routes = {}
    for bus in busses:
        if bus !='x':
            bus_routes['bus {0}'.format(bus)]= build_schedule(ts,int(bus))
    df = pd.DataFrame(data=bus_routes)

    series = df.loc[ts:].isin(['D']).any(axis=1)
    for i in range(ts,ts+479):
        if series.at[i]:
            print(i, ts-i)
            print(df.loc[i])

    print(df)

    # print(ts)
    # print(busses)

ts, busses = get_input()
pattern = []
counter = 0
for bus in busses:

    if bus == 'x':
        pattern.append(0)
    else:
        pattern.append(int(bus))
print(pattern)
matched = False
inc_by = 7
tick = 7
sub_inc =0
count = 0
# while True:
#     tick += inc_by
#     if(tick+1) % pattern[1] == 0:
#         print( count, tick, tick % pattern[0], (tick+1) % pattern[1])
#         count = 0
#     count+=1
tick = pattern[0]
inc_by = pattern[0]
sub_inc = 0
for p in pattern[1:]:
    sub_inc += 1
    if p != 0:
        while (tick + sub_inc) % p != 0:
            tick+= inc_by
        print( p, tick, sub_inc, inc_by)
        inc_by *= p
print(tick)






def try2():
    #pattern = [17,0,13,19]
    biggest = 1
    for p in pattern:
        if p > biggest:
            biggest = p

    tick = biggest - pattern.index(biggest)
    tick = biggest * 219298245614
    combined_ticker = biggest
    found_matches = {}

    for p in pattern:
        found_matches[p] = False
    while matched == False:
        sub_tick =0
        matched = True
        for p in pattern:
            if p != 0:
                if (tick + sub_tick) % p != 0:
                    matched = False
                    break
                else:
                    #print(p, tick, sub_tick, (tick+sub_tick) % p)
                    if found_matches[p] == False:
                        print('new match', p, tick)
                        found_matches[p] = True
                        #combined_ticker = tick
                    #found another link in the chain
            sub_tick +=1
        if matched:
            print('passes on', tick)
        else:
            tick += combined_ticker #ugly hack here


