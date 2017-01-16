import numpy as np

def solve():
    mat = [[np.inf] * 100 for _ in range(100)]

    for i in range(100):
        mat[i][i] = 0

    n, m, k = [int(x) for x in input().split()]
    s = [0] * (k+2)
    d = [0] * (k+2)

    for i in range(m):
        a, b, g = [int(x) for x in input().split()]
        mat[a-1][b-1] = min(g, mat[a-1][b-1])
        mat[b-1][a-1] = min(g, mat[a-1][b-1])

    for i in range(k):
        s[i+1], d[i+1] = [int(x)-1 for x in input().split()]

    for kk in range(n):
        for i in range(n):
            for j in range(n):
                if mat[i][j] > mat[i][kk] + mat[kk][j]:
                    mat[i][j] = mat[i][kk] + mat[kk][j]

    f = [[0]*2 for _ in range(k+2)]
    f[0][1] = np.inf
    d[0] = 0

    for i in range(1, k+1):
        f[i][0] = f[i-1][0] + mat[d[i-1]][s[i]] + mat[s[i]][d[i]]
        f[i][1] = f[i-1][0] + mat[d[i-1]][s[i]] + mat[s[i]][s[i+1]] + mat[s[i+1]][d[i]]
        f[i][0] = min(f[i][0], f[i-1][1] + mat[d[i-1]][d[i]])
        f[i][1] = min(f[i][1], f[i-1][1] + mat[d[i-1]][s[i+1]] + mat[s[i+1]][d[i]])

    return -1 if f[k][0] == np.inf else f[k][0]

t = int(input())

for i in range(1, t+1):
    print ('Case #%d: %d' % (i, solve()))
