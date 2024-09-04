from collections import defaultdict

N, K = map(int, input().split())
digit = len(str(N))
li = [int(s) for s in str(N)]

dp = [[defaultdict(int) for _ in range(2)] for _ in range(digit)]
# dp[i][smaller] 先頭から i 桁まで定めたときの, {積, 個数}
## 組合せ数としては意外と少ないのがポイント
# smaller == 1 なら N よりも真に小さい場合
# smaller == 0 なら N と i 桁まで一致する場合
dp[0][1][li[0]] += 1
for top in range(1, li[0]):
    dp[0][0][top] += 1
for i in range(1, len(li)):
    top = li[i]
    # smaller
    # smaller -> smaller は, 0 から 9 まで見てよい
    for k in range(10):
        for key, value in dp[i - 1][0].items():
            dp[i][0][k * key] += value
    # none -> smaller (先頭が i 桁目のもの)
    for k in range(1, 10):
        dp[i][0][k] += 1
    # equal -> smaller は i 桁目が 0 から top 未満
    for k in range(top):
        for key, value in dp[i - 1][1].items():
            dp[i][0][k * key] += value

    # equal -> equal は i 桁目は top
    for key, value in dp[i - 1][1].items():
        dp[i][1][top * key] += value

ans = 0
for key, value in dp[-1][0].items():
    if key <= K:
        ans += value
for key, value in dp[-1][1].items():
    if key <= K:
        ans += value

print(ans)
