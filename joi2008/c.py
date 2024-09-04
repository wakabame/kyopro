import bisect

N, M = map(int, input().split())
P = [0] + [int(input()) for _ in range(N)]

Q = sorted([p + q for p in P for q in P])

ans = 0
for q in Q:
    rem = M - q
    index = bisect.bisect(Q, rem)
    p = Q[index - 1]
    if p + q > M:
        continue
    ans = max(ans, p + q)

print(ans)
