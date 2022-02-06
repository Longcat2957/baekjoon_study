import sys
input = sys.stdin.readline
N = int(input())
# 배열의 크기
k = int(input())
# k는 min(10**9, N**2)보다 작거나 같은 자연수
# 문제의 조건으로 부터 NXN 행렬의 원소의 수는 최대 10**10이므로 
# 일반적인 풀이를 사용할 경우 메모리 초과 혹은 시간 초과가 발생한다.
# 따라서 이분탐색을 이용해 풀이한다.

# 각 행으로 부터
# 입력값 k 보다 작은 수의 개수는 다음과 같다.
# 1행의 경우 k 개(if k <= N) 또는 n 개 이다(if k > N)
# 2행의 경우 k //2 개 또는 n개 이다.

left, right = 1, N**2
while left <= right:
    mid = left + (right - left)//2
    cnt = 0
    # 여기서 cnt 는 k 보다 작은 값의 개수를 의미한다.
    
    for i in range(1, N+1):
        cnt += min(mid//i, N)
        # 각 행에 k값보다 작은 수의 개수는 위와 같다.
    
    if cnt >= k:
        right = mid - 1
        # 아직 k 개의 숫자에 도달하지 못했을 경우 범위를 좁힌다.
    
    else:
        left = mid + 1
        # k보다 더 큰 값이 나올 경우 범위를 넓힌다.
        
print(left)