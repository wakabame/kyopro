MOD = 10**9 + 7

s = input()
N = len(s)
# dp[i][k] ... i 文字目まで見て、chokudai の k 文字目まで作る通り数
dp = [[0 for _ in range(9)] for _ in range(N + 1)]
dp[0][0] = 1

st = ["c", "h", "o", "k", "u", "d", "a", "i"]
di = {}
for i, v in enumerate(st):
    di[v] = i + 1
for n in range(N):
    for k in range(9):
        dp[n + 1][k] = dp[n][k]
    v = s[n]
    if v in di:
        i = di[v]
        dp[n + 1][i] += dp[n][i - 1]
        dp[n + 1][i] %= MOD
print(dp[-1][-1])
