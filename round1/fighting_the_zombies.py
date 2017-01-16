t = int(input())

x = [[0] * 100 for _ in range(200)]

def solve():
    (n, r) = map(lambda x: int(x), input().split())
    x = [0] * n
    y = [0] * n

    sol = [set() for _ in range(n*n)]
    for i in range(n):
        (x[i], y[i]) = map(lambda x: int(x), input().split())

    for i in range(n):
        for j in range(n):
            for k in range(n):
                if x[i]<=x[k] and x[k]<=x[i]+r and y[j]<=y[k] and y[k]<=y[j]+r:
                    sol[i*n+j].add(k)

    finalset = set()
    for x in sol:
        finalset.add(frozenset(x))

    largest = 0
    for x in finalset:
        for y in finalset:
            p = x | y
            largest = max(largest, len(p))

    return largest

for i in range(1, t+1):
    print ('Case #%d: %d' % (i, solve()))
