import sys
import heapq
input = sys.stdin.readline

arr = []
answers = []
N = int(input())
for _ in range(N):
    number = int(input())
    if number == 0:
        if len(arr) == 0:
            answers.append(0)
        else:
            answers.append(heapq.heappop(arr)[1])
    
    elif number != 0:
        heapq.heappush(arr, (abs(number), number))

print(*answers, sep='\n')