with open('input.txt') as f:
    groups = []
    group = {'set':set(),'people':[]}
    for line in f:
        if line == '\n':
            groups.append(group)
            print(group['set'])
            group = {'set':set(),'people':[]}
        else:
            line = line.strip()
            group['people'].append(line)
            for char in line:
                group['set'].add(char)

    sum = 0
    for group in groups:
        answered_questions = group['set']
        for people in group['people']:
            answered_questions = answered_questions.intersection([p for p in people])
        sum += len(answered_questions)
        #     if len(people) < len(group['set']):
        #         print('no good', group)
        #         group_good = False
        # if group_good:
        #     sum+=len(group['set'])
print (sum)
