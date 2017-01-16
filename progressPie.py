import math

degtoRad = lambda x: x*(math.pi/180)
distance = lambda x, y: math.sqrt(x**2+y**2)

T = int(input())

for i in range(1, T + 1):
    (P, X, Y) = map(lambda x: int(x), input().split())
    pNew = degtoRad(P / 100.0 * 360)
    (xNew, yNew) = map(lambda x: x - 50, (X, Y))
    radian = math.atan2(xNew, yNew)
    radian = radian + math.pi * 2 if radian < 0 else radian;
    result = 'black' if distance(xNew, yNew) <= 50 and radian < pNew else 'white'
    print('Case #%d: %s' % (i, result))
