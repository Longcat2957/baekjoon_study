n = int(input())
list = list(map(int, input().split()))
min, max = min(list), max(list)
print(f'{min} {max}')