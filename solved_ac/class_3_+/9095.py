import sys
from math import factorial
input = sys.stdin.readline
T = int(input())
input_list = []
for _ in range(T):
    n = int(input())
    input_list.append(n)

def func_return_list(n:int):
    comb = []
    max_3 = n // 3
    max_2 = n // 2
    for i in range(max_3 + 1):
        for j in range(max_2 + 1):
            for k in range(n+1):
                if 3 * i + 2 * j + k == n:
                    comb.append([i,j,k])
    return comb

def list_to_case(combination_list:list):
    cnt = 0
    for list in combination_list:
        i, j, k = list
        cnt += (factorial(i+j+k))//(factorial(i) * factorial(j) * factorial(k))
    return cnt
answers = []
for i in input_list:
    answers.append(list_to_case(func_return_list(i)))
print(*answers,sep='\n')
    