import math


cache = {}

def calc(n, blank):
    if blank < 0:
        return 0;

    if blank in cache:
        return cache[blank];

    value = 1

    d0 = blank+n - (blank%n)
    d1 = blank+n-1 - (blank % (n-1))

    for x in range(blank+1,n+blank+1):
        value *= x
        if x == d0:
            value /= n
        if x == d1:
            value /= (n-1)

        value %= 1000000007

    cache[blank] = value

    return value


def solve():

    n, m = [int(x) for x in input().split()]

    x = [0] * n
    for i in range(n):
        x[i] = int(input())

    total = sum(x) * 2

    if n == 1:
        return m

    result = 0

    for i in range(n):
        for j in range(i + 1, n):
            result += 2*calc(n, (m-1)-(total-x[i]-x[j]))
            result %= 1000000007

    return result

T = int(input())

for i in range(1, T+1):
    cache = {}
    print ('Case #%d: %d'% (i, solve()))
