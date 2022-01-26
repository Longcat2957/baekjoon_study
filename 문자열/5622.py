def guess_number(input)-> int:
    if input in ['A', 'B', 'C']:
        return 3
    elif input in ['D', 'E', 'F']:
        return 4
    elif input in ['G', 'H', 'I']:
        return 5
    elif input in ['J', 'K', 'L']:
        return 6
    elif input in ['M', 'N', 'O']:
        return 7
    elif input in ['P','Q','R','S']:
        return 8
    elif input in ['T', 'U', 'V']:
        return 9
    elif input in ['W', 'X', 'Y', 'Z']:
        return 10
    else:
        return -1
input_list = input()
time = 0
for i in range(len(input_list)):
    time += guess_number(input_list[i])
print(time)