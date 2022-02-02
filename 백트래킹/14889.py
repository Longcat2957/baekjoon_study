import sys
input = sys.stdin.readline

N = int(input())
# 인원수를 입력받는다.
matrix = [[0 for col in range(N)] for row in range(N)]
# N*N 배열을 선언한다.
for row in range(N):
    matrix[row] = list(map(int, input().split()))
    # 한 줄씩 입력받고, 각 행에 저장한다.

# [0, 1, 2, 3]
# [4, 0, 5, 6]
# [7, 1, 0, 2]
# [3, 4, 5, 0]

# 총 인원수 N 명을 (N/2), (N/2)로 나누는 경우의 수는
# N Combination N/2 이다.
# 인원수의 상한은 20 명이므로 최대로 탐색하는 경우의 수는 20C10 이다.
# 양 팀의 숫자가 같으므로 전체 경우의 수는 20C10 / 2!

# 큰 값을 선언한다.

def combine(n):
    result = []
    
    def dfs(elements:list, start:int, k:int):
        if k == 0:
            result.append(set(elements[:]))
            return
        
        for i in range(start, n+1):
            elements.append(i)
            dfs(elements, i+1, k-1)
            elements.pop()
            # reset
    
    dfs([],2,n//2)
    return result

def find(n:int):
    combine_list = combine(n)
    answer = sys.maxsize
    for s in combine_list:
        set_u = set([i for i in range(1, N+1)]) - s
        list_a = list(s)
        list_b = list(set_u)
        sum_a, sum_b = 0, 0
        for i in range(n//2):
            for j in range(i+1, n//2):
                sum_a += matrix[list_a[i] - 1][list_a[j] - 1] + matrix[list_a[j] - 1][list_a[i] - 1]
        for i in range(n//2):
            for j in range(i+1, n//2):
                sum_b += matrix[list_b[i] - 1][list_b[j] - 1] + matrix[list_b[j] - 1][list_b[i] - 1]
        answer = min(answer, abs(sum_a - sum_b))
    
    print(answer)

find(N)