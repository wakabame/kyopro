from heapq import heappush, heappop

N, M, X, Y = map(int, input().split())

adj = [[] for i in range(N)]  # 始点を i とするedgeの集合
for _ in range(M):
    a, b, t, k = map(int, input().split())
    adj[a - 1] += [(b - 1, t, k)]
    adj[b - 1] += [(a - 1, t, k)]

distance = [float("inf") for i in range(N)]  # 頂点 i までの最短距離
distance[X - 1] = 0

confirm = [False] * N  # 頂点までの距離が確定しているか
hq = [(0, X - 1)]  # (頂点までの距離, 頂点のindex) のタプルを持つ

# ダイクストラ法
while hq:
    d, v = heappop(hq)
    if confirm[v]:
        continue
    confirm[v] = True
    for w, t, k in adj[v]:
        time_cost = (d + k - 1) // k * k + t - d
        if not confirm[w] and d + time_cost < distance[w]:
            distance[w] = d + time_cost
            heappush(hq, (distance[w], w))

if distance[Y - 1] == float("inf"):
    print(-1)
else:
    print(distance[Y - 1])
