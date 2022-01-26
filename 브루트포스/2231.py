import sys
n = sys.stdin.readline().strip()
int_n = int(n)
order = len(n)
def make(input:int) -> int:
    if input <= 0:
        return 0
    string = list(map(int, str(input)))
    buffer = 0
    for i in range(len(string)):
        buffer+= int(string[i])
    return input + buffer

result_list = []
for i in range(1, 9*order + 1):
    if make(int_n - i) == int_n:
        result_list.append(int_n - i)

if result_list == []:
    print(0)
else:
    print(min(result_list))