num_list = []
while True:
    try:
        num_list.append(int(input()))
    except:
        break
max = max(num_list)
print(max)
print(num_list.index(max)+1)