import sys
sys.setrecursionlimit(20 ** 5)
# DFS オイラーツアー
N = int(input())
C = [int(t)-1 for t in input().split()]
edges = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    edges[a-1] += [b-1]
    edges[b-1] += [a-1]

# その頂点に訪れるまでに使った色のリスト
collor_cnt = [0] * (10**5)

ans = []

def dfs(u=None, v=0):
    global ans
    if collor_cnt[C[v]] == 0:
        ans += [v]
    collor_cnt[C[v]] += 1

    for w in edges[v]:
        if w == u:
            continue
        dfs(v,w)

    collor_cnt[C[v]] -= 1

dfs()
ans.sort()
for v in ans:
    print(v+1)
