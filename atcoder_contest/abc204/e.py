# 時刻t でAiから Bi に行くと, Ci + Di//(t+1) 掛かる
# 待機時間 s すると, s + Ci + Di//(t+s+1) が距離になる
# これを最小化するように考える

from heapq import heappush, heappop

N, M = map(int, input().split())


def calc_best_time(d):
  ret_cand = []
  for time in range(int(d**0.5)-1, int(d**0.5) + 3):
    if time < 0:
      continue
    ret_cand += [[time+d//(time+1), time]]
  ret_cand.sort()

  return ret_cand[0][1]

adj = [[] for i in range(N)]  # 始点を i とするedgeの集合
for _ in range(M):
    a, b, c, d = map(int, input().split())
    bt = calc_best_time(d)
    adj[a - 1] += [(b - 1, c, d, bt)]
    adj[b - 1] += [(a - 1, c, d, bt)]

distance = [float("inf") for i in range(N)]  # 頂点 i までの最短距離
distance[0] = 0


confirm = [False] * N  # 頂点までの距離が確定しているか
# hq は [頂点kまでの最短距離, 頂点k] を要素に持つ
# ヒープキューのソートキーにするため、最短距離が第一変数
hq = [(0, 0)]
# ダイクストラ法
while hq:
    dist, v = heappop(hq)
    if confirm[v]:
        continue
    confirm[v] = True
    for w, c, d, best_time in adj[v]:
        wait_time = max(best_time - dist,0)
        cost = wait_time + c + d//(dist + wait_time + 1)
        if not confirm[w] and dist + cost < distance[w]:
            distance[w] = dist + cost
            heappush(hq, (distance[w], w))

if distance[-1] == float("inf"):
  print(-1)
else:
  print(distance[-1])
