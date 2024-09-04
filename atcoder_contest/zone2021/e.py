R, C = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(R)]
B = [list(map(int, input().split())) for _ in range(R - 1)]

from heapq import heappush, heappop

# i, j から左に行く コスト A[i][j-1]
# i, j から右に行く コスト A[i][j]
# i, j から 下に行く コスト B[i][j]
# i, j から上に a マス行くを実装すると辺が多くなりすぎるため, 以下で言い換える
## コスト １で裏面に移動
## 裏面ではコスト1で上に行ける・コスト0で表面に戻れる
# ダイクストラ
adj = [[] for k in range(2 * R * C)]  # 始点を k = i * C + j とする edgeの集合
for k in range(R * C):
    j = k % C
    i = k // C
    # 下に行く
    if i < R - 1:
        adj[k] += [(k + C, B[i][j])]
    # 上に行く
    adj[k] += [(R * C + k, 1)]
    adj[R * C + k] += [(k, 0)]
    if i > 0:
        adj[R * C + k] += [(R * C + k - C, 1)]
    # 左に行く
    if j > 0:
        adj[k] += [(k - 1, A[i][j - 1])]
    # 右に行く
    if j < C - 1:
        adj[k] += [(k + 1, A[i][j])]
distance_from_start = [float("inf") for i in range(2 * R * C)]  # 頂点 i までの最短距離
distance_from_start[0] = 0

confirm = [False] * (2 * R * C)  # 頂点までの距離が確定しているか
# hq は [頂点kまでの最短距離, 頂点k] を要素に持つ
# ヒープキューのソートキーにするため、最短距離が第一変数
hq = [(0, 0)]

# ダイクストラ法
while hq:
    d, v = heappop(hq)
    if confirm[v]:
        continue
    confirm[v] = True
    for w, c in adj[v]:
        if not confirm[w] and d + c < distance_from_start[w]:
            distance_from_start[w] = d + c
            heappush(hq, (distance_from_start[w], w))

print(distance_from_start[R * C - 1])
