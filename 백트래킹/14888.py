import sys
input = sys.stdin.readline
N = int(input())
numbers = list(map(int, input().split()))
operators = list(map(int, input().split()))

maximum = -1e9
minimum = 1e9
# 최대값, 최소값 한계를 입력

def dfs(depth, total, plus, minus, multiply, divide):
    global maximum, minimum
    if depth == N:
        maximum = max(total, maximum)
        minimum = min(total, minimum)
        return
    
    if plus > 0:
        dfs(depth + 1, total + numbers[depth], plus -1, minus, multiply, divide)
        # 위의 if 문이 종료되고 dfs(1, result, plus == 0, minus, multiply, divide) 상태가 되면 +를 제외한
        # 나머지 연산자를 이용한 조합이 연산된다.
    if minus > 0:
        dfs(depth + 1, total - numbers[depth], plus, minus - 1, multiply, divide)
    if multiply > 0:
        dfs(depth + 1, total * numbers[depth], plus, minus, multiply - 1, divide)
    if divide > 0:
        dfs(depth + 1, int(total / numbers[depth]), plus, minus, multiply, divide - 1)
        # '/'는 실수 나눗셈이므로 int형으로 변환하는 과정이 필요하다.

dfs(1, numbers[0], operators[0], operators[1], operators[2], operators[3])

print(maximum)
print(minimum)
