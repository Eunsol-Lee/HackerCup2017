def solve(N, W):
    move = 0
    used = 0
    W.sort()
    W.reverse()
    for j in range(N):
        count = int((50 - 0.000001) / W[j]) + 1;
        used += count;
        if used > N:
            return move

        move += 1

    return move


T = int(input())

for i in range(1, T+1):
    N = int(input())
    W = []
    for j in range(N):
        W.append(int(input()))

    print ('Case #%d: %d' % (i, solve(N, W)))
