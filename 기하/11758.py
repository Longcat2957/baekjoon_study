def ccw(point1:list, point2:list, point3:list):
    S = (point2[0] - point1[0])*(point3[1] - point1[1]) - (point2[1] - point1[1])*(point3[0] - point1[0])
    S *= 0.5
    if S > 0:
        return 1
    if S == 0:
        return 0
    if S < 0:
        return -1

a, b = map(int, input().split())
c, d = map(int, input().split())
e, f = map(int, input().split())
point1, point2, point3 = [a,b], [c,d], [e,f]

result = ccw(point1, point2, point3)
print(result)