from heapq import heappush, heappop

N, M = map(int, input().split())
edges = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    edges[a-1] += [b-1]
    edges[b-1] += [a-1]


dist = [float("inf") for i in range(N)]  # 頂点 i までの最短距離
dist[0] = 0

confirm = [False] * N  # 頂点までの距離が確定しているか
# hq は [頂点kまでの最短距離, 頂点k] を要素に持つ
# ヒープキューのソートキーにするため、最短距離が第一変数
hq = [(0, 0)]
# ダイクストラ法
while hq:
    d, v = heappop(hq)
    if confirm[v]:
        continue
    confirm[v] = True
    for w in edges[v]:
        if not confirm[w] and d + 1 < dist[w]:
            dist[w] = d + 1
            heappush(hq, (dist[w], w))

route_length = dist[-1]
if route_length == float("inf"):
    exit(print(0))


from collections import defaultdict
# length[i] 距離がiとなる頂点のset
length = defaultdict(set)
for i in range(N):
    if dist[i] != float("inf"):
        length[dist[i]].add(i)

ver_to_count = defaultdict(int)
ver_to_count[0] = 1
MOD = 10**9+7
for i in range(route_length):
    for u in length[i]:
        for v in edges[u]:
            if dist[v] != i+1:
                continue
            ver_to_count[v] += ver_to_count[u]
            ver_to_count[v] %= MOD

print(ver_to_count[N-1])
