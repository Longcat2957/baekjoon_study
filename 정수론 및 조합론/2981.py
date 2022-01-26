import sys
import math
n = int(input())
# 2 <= N <= 100
int_list = []
for i in range(n):
    int_list.append(int(sys.stdin.readline()))
int_list.sort()
min_value = int_list[0]
scd_value = int_list[1]

# 나머지의 범위 : i in range(min_value+1)
# 몫의 범위 : j in range(2, scd_value-1)

# 입력값과 나머지의 범위, 몫의 범위가 주어졌을 때 몫, 나머지 쌍의 갯수를 리턴하는 함수
def check(input:int, min_value:int, scd_value:int):
    result_list = []
    
    for i in range(min_value+1):
        for j in range(2, scd_value -1):
            if input % j == i:
                result_list.append([j, i])
    
    return result_list

def intersection(lst1:list, lst2:list):
    intersection = list(set([tuple(l) for l in lst1]) & set([tuple(l) for l in lst2]))
    
    return intersection

sample_list = intersection(check(int_list[0], min_value, scd_value), check(int_list[1], min_value, scd_value))
sample_result_list = []
for i in range(len(sample_list)):
    sample_result_list.append(sample_list[i][0])
sample_result_list.sort()

if n == 2:
    for i in sample_result_list:
        print(i, end = ' ')
elif n > 2:
    int_list = int_list[2::]
    for s in sample_result_list:
        for num in int_list:
            if min_value % s != num % s:
                sample_result_list.remove(s)
                break
        continue
    for i in sample_result_list:
        print(i, end = ' ')
        