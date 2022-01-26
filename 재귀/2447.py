import sys
sys.setrecursionlimit(10**6)
# 재귀를 사용해서 풀어야 하는 문제에서, 파이썬의 기본 재귀 깊이 제한은 1000이므로
# 위 코드를 이용해서 제한을 확장한다.

# 재귀 테크닉을 활용하기 위해 문제를 2개 이상의 작은 문제로 분할한 뒤
# 각각의 부분에서 문제를 해결하고, 결과를 통합한다.
# Divide -> Solve -> Conquer

n = int(sys.stdin.readline().strip())

# 크기 3의 패턴은 가운데에 공백이 있고, 가운데를 제외한 모든 칸에 별이
# 하나씩 있는 패턴이다.
def append_star(input:int):
    if input == 3:
        print('***')
        print('* *')
        print('***')




append_star(n)