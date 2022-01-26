import math
t = int(input())
empty_list = []
for c in range(t):
    empty_list.append(list(map(int, input().split())))

def find_min_path(a:int, b:int) -> int:
    distance = b-a
    max = 0
    while True:
        if distance <= max*(max+1):
            break
        max += 1
    if distance - max**2 <= 0:
        return 2*max -1
    elif distance - max**2 > 0:
        return 2*max



for i in range(t):
    print(find_min_path(empty_list[i][0], empty_list[i][1]))
