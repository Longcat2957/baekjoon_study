import string
input_string = input()
buffer_list = []
for num in range(len(string.ascii_lowercase)):
    buffer_list.append(int(input_string.count(string.ascii_lowercase[num])))
for num in range(len(string.ascii_uppercase)):
    buffer_list[num] += int(input_string.count(string.ascii_uppercase[num]))
if buffer_list.count(max(buffer_list)) >= 2:
    print('?')
else:
    print(string.ascii_uppercase[buffer_list.index(max(buffer_list))])