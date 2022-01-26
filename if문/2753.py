# 윤년을 계산하는 프로그램을 작성
num = int(input())
if num % 400 == 0:
    print(1)
elif num % 4 == 0 and num % 100 != 0:
    print(1)
else:
    print(0)