import math
t = int(input())
input_list = []
for i in range(t):
    x_1, y_1, r_1, x_2, y_2, r_2 = map(int, input().split())
    input_list.append([x_1, y_1, r_1, x_2, y_2, r_2])

def find_position(input:list)-> int:
    if input[0] == input[3] and input[1] == input[4]:
        if input[2] == input[5]:
            return -1
        elif input[2] != input[5]:
            return 0
    else:
        point_length = math.sqrt((input[0] - input[3])**2 + (input[1] - input[4])**2)
        r_1 = input[2]
        r_2 = input[5]
        empty_list = [float(r_1), float(r_2), point_length]
        empty_list.sort()
        if empty_list[2] > empty_list[0] + empty_list[1]:
            return 0
        elif empty_list[2] == empty_list[0] + empty_list[1]:
            return 1
        else:
            return 2
        
for i in range(t):
    print(find_position(input_list[i]))