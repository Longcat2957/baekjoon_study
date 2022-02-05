import sys
input = sys.stdin.readline

def mat_row_mul(p:int, q:int):
    row_a = mat_a[p]
    row_b = mat_b_t[q]
    length = len(row_a)
    sum = 0
    for l in range(length):
        sum += row_a[l] * row_b[l]
    return sum

a_n, a_m = map(int, input().split())
mat_a = [[0 for col in range(a_m)]for row in range(a_n)]
for r in range(a_n):
    column = list(map(int, input().split()))
    mat_a[r] = column

b_n, b_m = map(int, input().split())
mat_b = [[0 for col in range(b_m)]for row in range(b_n)]
for r in range(b_n):
    column = list(map(int, input().split()))
    mat_b[r] = column

# matrix B를 조금 변형하여 곱하기 좋은 형태로 바꾼다.
mat_b_t = [[0 for col in range(b_n)]for row in range(b_m)]
for i in range(b_n):
    for j in range(b_m):
        mat_b_t[j][i] = mat_b[i][j]
    
mat_c =[[0 for col in range(b_m)]for row in range(a_n)]
for i in range(a_n):
    for j in range(b_m):
        mat_c[i][j] = mat_row_mul(i,j)
        # 행간 곱셈을 함수로 선언하여 계산할 수 있도록 한다.

for i in range(a_n):
    print(*mat_c[i],sep = ' ')
