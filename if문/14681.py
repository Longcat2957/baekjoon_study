x = int(input())
y = int(input())
def where(num1, num2):
    if num1 > 0 and num2 > 0:
        print(1)
        return 0
    elif num1 < 0 and num2 > 0:
        print(2)
        return 0
    elif num1 < 0 and num2 < 0:
        print(3)
        return 0
    elif num1 > 0 and num2 < 0:
        print(4)
        return 0
    else:
        return 0
where(x, y)