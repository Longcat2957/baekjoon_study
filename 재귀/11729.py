import sys
sys.setrecursionlimit(10**8)

n = int(sys.stdin.readline())
def hanoi(n,a,b,c):
    if n == 1:
        print(a,c)
        # 한개의 블록이 남았다면 a에서 c로 이동시키기.
    else:
        hanoi(n-1,a,c,b)
        print(a,c)
        hanoi(n-1,b,a,c)
sum = 1
for i in range(n-1):
    sum = sum * 2 + 1
print(sum)
hanoi(n,1,2,3)