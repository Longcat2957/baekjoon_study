import sys
T = int(sys.stdin.readline())
fibonacci_table = [0, 1]
one_case = [0, 1]
zero_case = [1, 0]
def fibonacci(N:int):
    if len(fibonacci_table) > N:
        return fibonacci_table[N]
    while len(fibonacci_table) <= N:
        max_index = len(fibonacci_table) - 1
        fibonacci_table.append(fibonacci_table[max_index] + fibonacci_table[max_index - 1])
        one_case.append(one_case[max_index] + one_case[max_index - 1])
        zero_case.append(zero_case[max_index] + zero_case[max_index - 1])
    return fibonacci_table[N]
fibonacci(40)
num_list = []
for _ in range(T):
    num = int(sys.stdin.readline().strip())
    num_list.append(num)

for num in num_list:
    print("{} {}".format(zero_case[num], one_case[num]))