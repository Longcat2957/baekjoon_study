N = int(input())
for c in range(N):
    str = '*'*(c+1) + ' '*(N-c-1)
    print(str[::-1])