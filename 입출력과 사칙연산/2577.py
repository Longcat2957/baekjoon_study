num_list = []
result = 1
while True:
    try:
        num_list.append(int(input()))
    except:
        break
for i in range(len(num_list)):
    result *= num_list[i]
result = str(result)
for i in range(10):
    counter = 0
    for c in range(len(result)):
        if i == int(result[c]):
            counter += 1
    print(counter)