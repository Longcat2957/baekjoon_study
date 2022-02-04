import sys
input = sys.stdin.readline
result = []

def check(a:int, b:int):
    if a < b and b % a == 0:
        return 'factor'

    elif a > b and a % b == 0:
        return 'multiple'
    else:
        return 'neither'

while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    result.append(check(a,b))
    
print(*result, sep='\n')