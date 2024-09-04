N, K = map(int, input().split())

ans = 0
for i in range(K, N + 2):
    minima = i * (i - 1) // 2
    maxima = i * (2 * N - i + 1) // 2
    ans += maxima - minima + 1
    ans %= 10**9 + 7

print(ans)
