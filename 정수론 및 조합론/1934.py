import sys
from math import gcd
input = sys.stdin.readline

n = int(input())
# 테스트 케이스의 수
ans = []
for _ in range(n):
    a, b = map(int, input().split())
    ans.append((a * b)//(gcd(a,b)))
    
print(*ans, sep='\n')