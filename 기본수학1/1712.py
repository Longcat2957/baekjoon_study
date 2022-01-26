import math
a, b, c = map(float, input().split())
if b >= c:
    print(-1)
else:
    if (a/(c-b)) == math.ceil(a/(c-b)):
        print(int(a/(c-b) + 1))
    else:
        print(int(math.ceil(a/(c-b))))