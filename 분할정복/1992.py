import sys
input = sys.stdin.readline
length_of_square_origin = int(input())
square_length_list = [1, 2, 4, 8, 16, 32, 64]
square_origin = []
for _ in range(length_of_square_origin):
    string = input().strip()
    # map(int, ....)로 받으면 0이 삭제되는 문제가 있어 먼저 스트링으로 받는다.
    one_of_col = []
    for i in range(length_of_square_origin):
        c = string[i]
        one_of_col.append(int(c))
    square_origin.append(one_of_col)

def solution_for_sub(square:list):
    length_of_square = len(square)
    # 사각형을 함수의 입력으로 받아 한 변의 길이를 받아 변수에 저장한다.
    sum = 0
    if length_of_square in square_length_list:
        # 사각형 한 변의 길이가 2**k(k는 1이상 7 이하의 자연수) 일 경우
        for i in range(length_of_square):
            for j in range(length_of_square):
                sum += square[i][j]
    if sum == length_of_square ** 2:
        return True
        # 사각형의 모든 성분이 1일 경우 True(1)를 리턴한다.
    elif sum == 0:
        return 2
        # 사각형의 모든 성분이 0일 경우 2를 리턴한다.
    else:
        return False
    

# 아직 문제푸는중 ㅠ