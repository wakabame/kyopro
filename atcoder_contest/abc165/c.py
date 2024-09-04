N, M, Q = map(int, input().split())
a, b, c, d = [], [], [], []
for i in range(Q):
    a_, b_, c_, d_ = map(int, input().split())
    a += [a_ - 1]
    b += [b_ - 1]
    c += [c_]
    d += [d_]


def score(A):
    ret = 0
    for i in range(Q):
        if A[b[i]] - A[a[i]] == c[i]:
            ret += d[i]
    return ret


def dfs(li):
    if len(li) == N:
        global ans
        ans = max(ans, score(li))
    else:
        if li == []:
            st = 1
        else:
            st = li[-1]
        for i in range(st, M + 1):
            li.append(i)
            dfs(li)
            li.pop()


ans = 0
dfs([])
print(ans)
