def solve_dp(s):
    n = len(s)
    s = [int(c) for c in s]
    inf = 10**9

    dp = [[inf] * 2 for _ in range(n)]

    d0 = s[0]
    dp[0][0] = d0
    dp[0][1] = d0 + 1

    for i in range(1, n):
        d = s[i]
        for k in range(10):
            if d + k >= 10:
                dp[i][0] = min(dp[i][0], dp[i - 1][1] + 2 * k + d - 10)
            else:
                dp[i][0] = min(dp[i][0], dp[i - 1][0] + 2 * k + d)
        d += 1
        for k in range(10):
            if d + k >= 10:
                dp[i][1] = min(dp[i][1], dp[i - 1][1] + 2 * k + d - 10)
            else:
                dp[i][1] = min(dp[i][1], dp[i - 1][0] + 2 * k + d)

    return dp[n - 1][0]


if __name__ == "__main__":
    s = input()
    s = "0" + s
    print(solve_dp(s))
