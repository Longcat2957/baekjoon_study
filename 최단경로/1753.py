import sys
input = sys.stdin.readline

V, E = map(int, input().split())
list_of_point = [i for i in range(1, V+1)]
# 정점의 개수 V와 간선의 개수 E
start = int(input())
# 시작 정점의 번호

list_of_point.remove(start)
# remove에 의해 시작 정점이 삭제 된다.

# 그래프를 어떤 자료구조로 표현할 것인가?
# 우선순위 큐(힙)을 적용한 다익스트라 알고리즘을 사용한다.

for end in list_of_point:
    # 시작 정점을 제외한 모든 도착 점을 end로 호출
    pass

# 아직 개념 공부중 ㅠ
# 20220205 16:21:54
