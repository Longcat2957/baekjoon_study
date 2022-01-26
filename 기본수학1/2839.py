n = int(input())
def sugar(input:int)-> int:
    buffer = input
    num1, num2 = 0, 0
    while True:
        if num2 == 5 or buffer < 0 :
            return -1
        if buffer % 5 == 0:
            num1 = buffer // 5
            return num1 + num2
        else:
            buffer -= 3
            num2 += 1
print(sugar(n))