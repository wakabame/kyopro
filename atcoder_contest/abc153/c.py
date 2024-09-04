N, K = map(int, input().split())
H = list(map(int, input().split()))
H.sort(reverse=1)

ans = 0
for i in range(N):
    if i < K:
        ans += 0
    else:
        ans += H[i]

print(ans)
