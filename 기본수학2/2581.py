min_num = int(input())
max_num = int(input())
empty_list = []
for c in range(min_num, max_num+1, 1):
    empty_list.append(int(c))
def find_prime_number(input_list:list) -> list:
    result_list = []
    for c in range(len(input_list)):
        buffer = input_list[c]
        flag = True
        if buffer == 1:
            continue
        elif buffer == 2:
            result_list.append(buffer)
            continue
        else:
            for i in range(2, input_list[c]):
                if input_list[c] % i == 0:
                    flag = False
        if flag == True:
            result_list.append(buffer)
    return result_list

def print_sum_min(input_list:list) -> str:
    result_list = find_prime_number(input_list)
    if result_list == []:
        print(-1)
    else:
        print(sum(result_list))
        print(min(result_list))

print_sum_min(empty_list)