def d(input: int, list: list) -> int:
    result = 0
    buffer_list = str(input)
    for num in buffer_list:
        result += int(num)
    if input+result not in list:
        list.append(input+result)
    if input + result >= 10001:
        return
    if input+result in list:
        return
    d(input+result, list)
empty_list = []
u = []
for c in range(1, 10001, 1):
    u.append(int(c))
for num in range(1, 10001, 1):
    d(num, empty_list)
result_list = list(set(u) - set(empty_list))
result_list.sort()
for num in range(len(result_list)):
    print(result_list[num])