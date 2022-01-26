import sys
N = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))
answer = [-1] * N
stack = []
stack.append(0)

for i in range(1, N):
    # i = 1, 2, 3, ... N-1
    while stack and array[stack[-1]] < array[i]:
        answer[stack.pop()] = array[i]
    stack.append(i)
    
for ans in range(N-1):
    print(answer[ans], end=" ")
print(answer[-1])
