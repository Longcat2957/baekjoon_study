n = int(input())

def fibonacci(input:int) -> int:
    if input == 0:
        return 0
    elif input == 1:
        return 1
    list = [0, 1]
    counter = 0
    while True:
        if counter == input - 1:
            return list[1]
        list.append(list[0] + list[1])
        list = list[1:]
        counter += 1

print(fibonacci(n))