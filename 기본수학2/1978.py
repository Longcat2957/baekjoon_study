N = int(input())
empty_list = list(map(int, input().split()))
def find_prime_number(input_list:list) -> int:
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
    return int(len(result_list))

print(find_prime_number(empty_list))