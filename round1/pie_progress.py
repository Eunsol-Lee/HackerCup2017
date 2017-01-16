# Hacker Cup 2017 Round 1
# Pie Progress by Eunsol

def solve():
    (n, m) = map(lambda x: int(x), input().split())
    now = [];
    cost = 0
    for i in range(n):
        c = list(map(lambda x: int(x), input().split()))
        c.sort()
        count = 0
        for x in c:
            count += 1
            value = count ** 2 + x - (count - 1) ** 2
            now.append(value)
        now.sort()
        cost += now.pop(0)

    return cost

T = int(input())

for i in range(1, T+1):
    print ('Case #%d: %d'% (i, solve()))
