import re

table = [[[0] * 401 for _ in range(21)] for _ in range(21)]

for i in [4, 6, 8, 10, 12, 20]:
    table[i][1] = [1] * (i + 1)
    table[i][1][0] = 0;
    for j in range(2, 21):
        for k in range(1, j * i + 1):
            for l in range(1, i + 1):
                if k - l >= 1 and k - l <= i * (j - 1):
                    table[i][j][k] += table[i][j - 1][k - l]

T = int(input())

pat = re.compile('(\d+)d(\d+)([+-]\d+)*')


for i in range(1, T + 1):
    X, Y, Z, O = [0] * 10, [0] * 10, [0] * 10, [0] * 10;

    maxV = 0;

    (H, S) = map(lambda x: int(x), input().split())
    result = pat.findall(input())
    for j in range(S):
        X[j] = int(result[j][0]);
        Y[j] = int(result[j][1]);
        if (result[j][2] != ''):
            Z[j] = int(result[j][2]);

        count = 0;
        total = 0;
        h = H - Z[j]
        h = 0 if h < 0 else h

        #print(X[j], Y[j], h)
        for k in range(h, X[j] * Y[j] + 1):
            count += table[Y[j]][X[j]][k];
        for k in range(0, X[j] * Y[j] + 1):
            total += table[Y[j]][X[j]][k];

        maxV = max(maxV, float(count)/float(total))
        #print (count, total)
        #print(table[Y[j]][X[j]])
    print ('Case #%d: %.6f' % (i, maxV))
