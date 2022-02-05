# 분할 정복은 다중 분기 재귀를 기반으로 하는 알고리즘 디자인 패러다임을 말한다.
import sys
square_length_list = [1, 2, 4, 8, 16, 32, 64, 128]
input = sys.stdin.readline

# 부분 문제 해결 방법
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
    elif sum == 0:
        return 2
    else:
        return False

def divide(square:list):
    result = []
    if solution_for_sub(square) == False and len(square) > 1:
        # 사각형의 모든 부분이 1로 채워져 있지 않으면서 한 변의 길이가 1이 아닌 경우
        length_half = len(square) // 2
        for i in range(2):
            for j in range(2):
                # 분할 이후 4개의 작은 사각형으로 나뉘게 된다.
                sub_list = []
                for ii in range(length_half):
                    sub_row = []
                    for jj in range(length_half):
                        sub_row.append(square[i * length_half + ii][j * length_half + jj])
                    sub_list.append(sub_row)
                result.append(sub_list)
    return result    

def check_list_of_square(list_of_squares:list):
    yes, no = 0, 0
    while list_of_squares:
        sq = list_of_squares.pop(0)
        if solution_for_sub(sq) == False:
            list_of_squares.extend(divide(sq))
        elif solution_for_sub(sq) == True:
            yes += 1
        elif solution_for_sub(sq) == 2:
            no += 1
    print(no)
    print(yes)
    
square_length_origin = int(input())
square = []
for _ in range(square_length_origin):
    square.append(list(map(int, input().split())))
square_list= []
square_list.append(square)

check_list_of_square(square_list)