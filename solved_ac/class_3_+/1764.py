import sys
N, M = map(int, sys.stdin.readline().split())
set_a, set_b = set(), set()
for _ in range(N):
    set_a.add(sys.stdin.readline().strip())

for _ in range(M):
    set_b.add(sys.stdin.readline().strip())

set_c = list(set_a & set_b)
print(len(set_c))
set_c.sort()
print(*set_c,sep='\n')
