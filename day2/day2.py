

with open('input.txt', 'r') as f:
    numbers = list()
    valid_pw = 0
    valid_pw_part_2 = 0
    for x in f:
        line = x.split(' ')
        min_pw = int(line[0].split('-')[0])
        max_pw = int(line[0].split('-')[1])
        char = line[1][0]
        pw = line[2].strip()
        if max_pw-1 < len(pw):
            lower = pw[min_pw-1]
            upper = pw[max_pw-1]
            print(lower, upper, char, line)
            if lower == char and upper != char:
                valid_pw_part_2 +=1
            elif lower != char and upper == char:
                valid_pw_part_2 +=1


        count = 0
        for pw_char in pw:
            if char == pw_char:
                count+=1
        if count >= min_pw and count <= max_pw:
            valid_pw +=1
    print( valid_pw)
    print( valid_pw_part_2)
