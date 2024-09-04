N, M, X = map(int, input().split())
C, A = [], []

for i in range(N):
    c, *a = map(int, input().split())
    C.append(c)
    A.append(a)

ans = float("inf")
for j in range(1 << N):
    curr = 0
    score = [0] * M
    for k in range(N):
        if 1 << k & j:
            curr += C[k]
            for m in range(M):
                score[m] += A[k][m]

    if min(score) >= X:
        ans = min(curr, ans)

if ans == float("inf"):
    print(-1)
else:
    print(ans)
