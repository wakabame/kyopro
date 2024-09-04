MOD = 10**9 + 7

N = int(input())
A = list(map(int, input().split()))

# dp[i][j] ... A の先頭 i 項を j 個の部分列に分割するときの通り数
dp = [[0 for i in range(N + 1)] for _ in range(N + 1)]
dp[0][0] = 1

cumsum = [0]
# cumsum[i] = sum(A[:i]) なる A についての累積和
for i in range(N):
    cumsum += [cumsum[-1] + A[i]]

# memo[j][k] ... j 分割を行ったときの総和を j で割った余りが k になるような通り数（途中経過）
memo = [[0 for i in range(N + 1)] for _ in range(N + 1)]
memo[1][0] = 1

for i in range(N):
    for j in range(N):
        dp[i + 1][j + 1] = memo[j + 1][cumsum[i + 1] % (j + 1)]

    for j in range(N - 1):
        memo[j + 2][cumsum[i + 1] % (j + 2)] += dp[i + 1][j + 1]
        memo[j + 2][cumsum[i + 1] % (j + 2)] %= MOD

print(sum(dp[-1]) % MOD)
