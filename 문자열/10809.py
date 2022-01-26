import string
input_list = list(input())
empty_list = []
for num in range(len(string.ascii_lowercase)):
    if string.ascii_lowercase[num] in input_list:
        empty_list.append(input_list.index(string.ascii_lowercase[num]))
    elif string.ascii_lowercase[num] not in input_list:
        empty_list.append(-1)
for i in range(len(empty_list)):
    print(empty_list[i], end = ' ')