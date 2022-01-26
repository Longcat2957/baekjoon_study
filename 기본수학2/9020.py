import math
n = int(input())
input_list = []

for c in range(n):
    input_list.append(int(input()))
def make_prime_list(input_list:list)->list:
    result_list = []
    max_int = max(input_list)
    for i in range(2, max_int + 1):
        max_value = round(math.sqrt(i))
        flag = True
        for j in range(2, max_value+1):
            if i % j == 0:
                flag = False
                break
        if flag == True:
            result_list.append(i)
    return result_list

def find_prime_pair(input_int:int, prime_list:list)->str:
    difference = 0
    while True:
        if (input_int - 2*difference)//2 in prime_list and (input_int + 2*difference)//2 in prime_list:
            num1 = (input_int - 2*difference)//2
            num2 = (input_int + 2*difference)//2
            return str(num1) + ' ' + str(num2)
            break
        difference += 1
prime_list = make_prime_list(input_list)
for i in range(n):
    print(find_prime_pair(input_list[i], prime_list))