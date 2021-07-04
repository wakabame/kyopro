# よく考えたらワーシャルフロイドそのもの
N, M = map(int, input().split())

edges = [[] for _ in range(N)]
for i in range(M):
    a, b, c = map(int, input().split())
    edges[a-1] += [[b-1, c]]

dist = [[10**9 for _ in range(N)] for _ in range(N)]
# 直通で行けるルートを初期コストと見なす
for i in range(N):
    dist[i][i] = 0
    for b, c in edges[i]:
        dist[i][b] = c

ans = 0
for i in range(N):
    # 頂点iを経由してよい
    for s in range(N):
        for t in range(N):
            dist[s][t] = min(dist[s][t], dist[s][i]+dist[i][t])
            if dist[s][t] != 10**9:
                ans += dist[s][t]

print(ans)
