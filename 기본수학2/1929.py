import math
num1, num2 = map(int, input().split())
empty_list = []
for i in range(num1, num2+1):
    max_value = round(math.sqrt(i))
    flag = True
    for c in range(2, max_value+1):
        if i % c == 0:
            flag = False
            break
    if flag == True:
        empty_list.append(i)
if 1 in empty_list:
    empty_list.remove(1)
for c in range(len(empty_list)):
    print(empty_list[c])