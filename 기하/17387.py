def ccw(point1:list, point2:list, point3:list):
    S = (point2[0] - point1[0])*(point3[1] - point1[1]) - (point2[1] - point1[1])*(point3[0] - point1[0])
    S *= 0.5
    if S > 0:
        return 1
    if S == 0:
        return 0
    if S < 0:
        return -1

a, b, c, d = map(int, input().split())
e, f, g, h = map(int, input().split())
p1, p2, p3, p4 = [a,b], [c,d], [e,f], [g,h]

flag = False
ans = 0
if ccw(p1,p2,p3) * ccw(p1,p2,p4) == 0 and ccw(p3,p4,p1) * ccw(p3,p4,p2) == 0:
    # 4개의 점이 모두 한 직선 위에 있을 경우
    flag = True
    if min(a,c) <= max(e,g) and min(e,g) <= max(a,c) and min(b,d) <= max(f,h) and min(f,h) <= max(b,d):
        ans = 1
if ccw(p1,p2,p3) * ccw(p1,p2,p4) <=0 and ccw(p3,p4,p1) * ccw(p3,p4,p2) <= 0:
    if not flag:
        ans = 1
print(ans)