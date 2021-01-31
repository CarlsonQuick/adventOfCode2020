


with open('input.txt', 'r') as f:
    numbers = list()
    for x in f:
        numbers.append(int(x))
    numbers.sort()

    upper = 2
    mid = 1
    lower = 0

    for low in range(0,len(numbers)-1):
        for mid in range(1, len(numbers) -1):
            for top in range(2, len(numbers)-1):
                if numbers[low] + numbers[mid] + numbers[top] == 2020:
                    print( numbers[low], numbers[mid], numbers[top], numbers[low] *numbers[mid] * numbers[top])

    # while numbers[lower] + numbers[mid] + numbers[upper] != 2020:
    #     print('{0}, + {1} = {3}, factor = {2}'.format(numbers[lower], numbers[upper], numbers[lower] * numbers[upper], numbers[upper] + numbers[lower]))
    #
    #     elif numbers[lower] + numbers[mid] + numbers[upper] > 2020:#big reset
    #         lower =mid
    #         mid = lower + 1
    #         upper = lower + 2
    #     else:
    #         while numbers[lower] + numbers[mid] + numbers[upper] < 2020:
    #
    #             upper +=1


    print('{0}, + {1} = {3}, factor = {2}'.format(numbers[lower], numbers[upper], numbers[lower] * numbers[upper], numbers[upper] + numbers[lower]))



