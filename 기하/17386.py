import sys

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
point1, point2, point3, point4 = [a,b], [c,d], [e,f], [g,h]

if ccw(point1, point2, point3) * ccw(point1, point2, point4) < 0:
    if ccw(point3, point4, point1) * ccw(point3, point4, point2) < 0:
        print(1)
    else:
        print(0)
else:
    print(0)