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

    val = [[np.inf] * (k + 1) for _ in range(2)]
    pos = [[-1] * (k + 1) for _ in range(2)]
    val[0][0] = 0
    pos[0][0] = 0
    for i in range(1,k+1):
        val[i][0] = val[i-1][0]+mat[pos[i-1][0]][mov[i-1][0]]+mat[mov[i-1][0]][mov[i-1][1]]
        pos[i][0] = mov[i-1][1]
        if i >= 2:
            v = val[i-1][1]+mat[pos[i-1]][mov[i-1][0]]+mat[mov[i-1][0]][mov[i-2][1]]+mat[mov[i-2][1]][mov[i-1][1]]
            if v < val[i][0]:
                val[i][0] = v
                pos[i][0]=mov[i-1][1]

        val[i][1] = val[i-1][0]+mat[pos[i-1][0]][mov[i-1][0]]
        pos[i][0] = mov[i-1][0]
        if i >= 2:
            v = val[i-1][1]+mat[pos[i-1]][mov[i-1][0]]+mat[mov[i-1][0]][mov[i-2][1]]
            if v < val[i][1]:
                va[i][1] = v
                pos[i][1] = mov[i-2][1]

    return -1 if value[i] == np.inf else value[i]

for i in range(1, t+1):
    print ('Case #%d: %d' % (i, solve()))
