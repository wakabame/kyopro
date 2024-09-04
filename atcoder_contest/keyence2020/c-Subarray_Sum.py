N, K, S = map(int, input().split())

if S == 10**9:
    print(" ".join(map(str, ([S] * K + [1] * (N - K)))))
else:
    print(" ".join(map(str, ([S] * K + [S + 1] * (N - K)))))
