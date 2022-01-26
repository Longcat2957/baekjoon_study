result = []
while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    result.append(a+b)
for c in range(len(result)):
    print(result[c])