n = int(input())
empty_list = []
for c in range(n):
    empty_list.append(list(map(int, input().split())))
for i in range(len(empty_list)):
    number = 0
    sum = 0
    upper = 0
    for c in range(len(empty_list[i])):
        if c == 0:
            number = empty_list[i][c]
        else:
            sum += empty_list[i][c]
    ave = sum/number
    for c in range(len(empty_list[i])):
        if c == 0:
            pass
        else:
            if ave < empty_list[i][c]:
                upper += 1
            else:
                pass
    str = "{:.3f}%".format((100*upper)/number)
    print(str)