x_list, y_list = [], []
for i in range(3):
    a, b = map(int, input().split())
    x_list.append(a)
    y_list.append(b)

x_1, y_1 = 0, 0
for i in range(3):
    if x_list.count(x_list[i]) == 1:
        x_1 = x_list[i]
    if y_list.count(y_list[i]) == 1:
        y_1 = y_list[i]

print(x_1, y_1)