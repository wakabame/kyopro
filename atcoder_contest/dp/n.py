N = int(input())
A = list(map(int, input().split()))

# dp[i][j]: i から j までの区間 [i,j] での最良スコア
# dp[0][N-1] が答えになる
dp = [[float("inf") for _ in range(N)] for _ in range(N)]
weight = [0]
for i in range(N):
    weight += [weight[-1] + A[i]]
for i in range(N):
    dp[i][i] = 0


for h in range(N): # 幅 h = j - i について考える
    for i in range(N-h):
        j = i + h
        for k in range(i, j): # [i,j] を [i,k], [k+1, j] に分割する
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + weight[j+1] - weight[i])

print(dp[0][-1])
