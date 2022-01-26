n = int(input())
empty_list = []
for i in range(n):
    empty_list.append(list(map(int, input().split())))

def return_room_number(H:int, W:int, N:int)->str:
    if int(N%H) == 0:
        room_number = int(N // H)
    else:
        room_number = int(1+ N//H)
    if int(N%H) == 0:
        floor_number = int(H)
    else:
        floor_number = int(N % H)
    if room_number < 10:
        return str(floor_number) + '0' + str(room_number)
    else:
        return str(floor_number) + str(room_number)

for i in range(n):
    print(return_room_number(empty_list[i][0], empty_list[i][1], empty_list[i][2]))