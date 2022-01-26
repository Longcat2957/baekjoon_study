import sys
import math

x1, y1, r1, x2, y2, r2 = map(float, sys.stdin.readline().split())
d = math.dist([x1,y1],[x2,y2])

def func(r,theta):
    result = 0.5 * (r**2) * theta - 0.5 * (r**2) * math.sin(theta)
    return result

if d >= r1 + r2:
    # 두 원이 서로 교차하는 영역이 없을 경우
    print('0.000')
elif d + min(r1, r2) <= max(r1, r2):
    s = round(math.pi * (min(r1, r2))**2,3)
    print(s)
else:
    
    theta_1 = 2*math.acos((d**2+r1**2-r2**2)/(2*r1*d))
    theta_2 = 2*math.acos((d**2+r2**2-r1**2)/(2*r2*d))

    s_1 = func(r1, theta_1)
    s_2 = func(r2, theta_2)
    s = s_1 + s_2
    print('%.3f'%s)

