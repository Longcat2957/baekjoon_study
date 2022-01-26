import sys
layer = int(sys.stdin.readline())
triangle_arr = []
for _ in range(layer):
    triangle_arr.append(list(map(int, sys.stdin.readline().split())))

for l in range(layer - 1):
    upper_layer, lower_layer = triangle_arr[l], triangle_arr[l+1]
    if len(upper_layer) == 1:
        u = upper_layer[0]
        for j in range(len(lower_layer)):
            lower_layer[j] += u
    elif len(upper_layer) > 1:
        lower_layer[0] += upper_layer[0]
        lower_layer[-1] += upper_layer[-1]

for l in range(1, layer - 1):
    upper_layer, lower_layer = triangle_arr[l], triangle_arr[l+1]
    for j in range(len(upper_layer) - 1):
        lower_layer[j + 1] = max(lower_layer[j + 1] + upper_layer[j], lower_layer[j + 1] + upper_layer[j+1])

print(max(triangle_arr[-1]))