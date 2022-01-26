# 시험성적을 입력받아 90~100점은 ....
def convert_score(score):
    if score >= 90:
        print('A')
        return 0
    elif score >= 80:
        print('B')
        return 0
    elif score >= 70:
        print('C')
        return 0
    elif score >= 60:
        print('D')
        return 0
    else:
        print('F')
        return 0

convert_score(int(input()))