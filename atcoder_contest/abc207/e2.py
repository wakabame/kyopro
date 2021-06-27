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

for i in range(N):
    for j in range(N):
        for k in range(1, i+2):
            # 最後の区間幅をkと考える
            # A[i+1-k] から A[i] までの総和が j+1 のときに, 合算
            if (cumsum[i+1] - cumsum[i+1-k]) % (j + 1) == 0:
                dp[i + 1][j + 1] += dp[i + 1- k][j]
                dp[i + 1][j + 1] %= MOD

print(sum(dp[-1])%MOD)
