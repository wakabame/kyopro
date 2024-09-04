count = 9
dp = [[[str(i)] for i in range(10)] for j in range(100)]
ans = [i for i in range(1, 10)]

keta = 0
while count < 10**5:
    for i in range(10):
        curr = []
        for elem in dp[keta][i]:
            top = int(elem[0])
            if top > 0:
                curr += [str(top - 1) + elem]
                if top > 1:
                    ans += [int(str(top - 1) + elem)]
            if top < 9:
                curr += [str(top + 1) + elem]
                ans += [int(str(top + 1) + elem)]
            curr += [str(top) + elem]
            if top > 0:
                ans += [int(str(top) + elem)]
        dp[keta + 1][i] = curr
        count += len(curr)
    keta += 1

ans.sort()

K = int(input())
print(ans[K - 1])
