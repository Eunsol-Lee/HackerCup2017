import numpy as np


t = int(input())



def solve():
    mat = [[np.inf] * 200 for _ in range(200)]

    for i in range(200):
        mat[i][i] = 0

    n, m, k = [int(x) for x in input().split()]
    mov = []

    for i in range(m):
        a, b, g = [int(x) for x in input().split()]
        mat[a-1][b-1] = min(g, mat[a-1][b-1])
        mat[b-1][a-1] = min(g, mat[a-1][b-1])

    for j in range(k):
        s, d = [int(x) for x in input().split()]
        mov.append((s-1, d-1))

    for kk in range(n):
        for i in range(n):
            for j in range(n):
                if mat[i][j] > mat[i][kk] + mat[kk][j]:
                    mat[i][j] = mat[i][kk] + mat[kk][j]

    value = [np.inf] * (k + 1)
    position = [-1] * (k + 1)
    value[0] = 0
    position[0] = 0
    for i in range(1,k+1):

        value[i] = value[i-1]+mat[position[i-1]][mov[i-1][0]]+mat[mov[i-1][0]][mov[i-1][1]]
        position[i] = mov[i-1][1]
        if i >= 2:
            v = value[i-2]+mat[position[i-2]][mov[i-2][0]]+mat[mov[i-2][0]][mov[i-1][0]]+mat[mov[i-1][0]][mov[i-2][1]]+mat[mov[i-2][1]][mov[i-1][1]]
            if v < value[i]:
                value[i] = v

    print (value, position)
    return -1 if value[i] == np.inf else value[i]

for i in range(1, t+1):
    print ('Case #%d: %d' % (i, solve()))
