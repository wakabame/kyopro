from collections import defaultdict
N, X, M = map(int, input().split())

# 値が何回目に現れたか, そこまでのsum をメモする
d = defaultdict(int)
d[X] = [1, X]


def f(x):
    return (x*x)%M

ans = X
for i in range(2, N+1):
    # i ボタンを押した回数
    X = f(X)
    if X in d:
        period = i - d[X][0]
        loop, rem = (N - i)//period, (N - i)%period
        ans += X
        ans += loop * (ans - d[X][1])
        for p in range(rem):
            X = f(X)
            ans += X
        exit(print(ans))
    ans += X
    d[X] = [i, ans]
print(ans)
