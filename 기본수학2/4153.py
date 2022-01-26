input_list = []
while True:
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break
    else:
        input_list.append([a, b, c])

def pitagorian(input:list) -> str:
    buffer_list = sorted(input)
    max_length = buffer_list[2]
    buffer_list = buffer_list[0:2]
    if max_length ** 2 - buffer_list[0] ** 2 - buffer_list[1] ** 2 == 0:
        print("right")
    else:
        print("wrong")

for i in range(len(input_list)):
    pitagorian(input_list[i])