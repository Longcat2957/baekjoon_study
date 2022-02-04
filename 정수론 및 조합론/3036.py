import sys
from math import gcd
input = sys.stdin.readline

N = int(input())
rings = list(map(int, input().split()))
first_ring = rings[0]
answers = []
for i in range(1, N):
    g = gcd(first_ring, rings[i])
    answer = str(first_ring//g)+'/'+str(rings[i]//g)
    answers.append(answer)

print(*answers, sep='\n')