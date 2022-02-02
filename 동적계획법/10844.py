import sys
input = sys.stdin.readline
N = int(input())
array = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
while N - 1:
    next_arr = []
    next_arr.append(array[1])
    for i in range(8):
        next_arr.append(array[i] + array[i+2])
    next_arr.append(array[8])
    array = next_arr[:]
    N -= 1

print(sum(array) % 1000000000)