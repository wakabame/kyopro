from collections import defaultdict, deque

N = int(input())
S = [input() for _ in range(N)]

# 先頭, 末尾3文字が同じものは同一視するため, set で管理する
path_di = defaultdict(set)
rev_path_di = defaultdict(set)
# 空になったら距離が確定できる
unused_path_di = defaultdict(set)

for s in S:
    st = s[:3]
    en = s[-3:]
    unused_path_di[st].add(en)
    path_di[st].add(en)
    rev_path_di[en].add(st)

# dist["最後の三文字"] = "勝てるか"
dist = defaultdict(lambda: -1)
# 次のステップで確定できるものを queue にいれる
q = deque()
for v in rev_path_di.keys():
    if len(path_di[v]) == 0:
        q.append(v)


# path[v] を使って, 頂点 v の距離を確定させる
## 0 が一つでもあれば 1(相手を負けさせられる). そうでないければ 0
# rev_path_di[v] をみて, 始点 u について unused_path_di[u] から v を消す
# v が 0 なら勝ち確定, unused_path_di[u] が空なら勝敗確定するので, u をappendする
while q:
    v = q.popleft()
    if dist[v] != -1:
        continue

    lose_flag = all([dist[w] for w in path_di[v]])
    dist[v] = 1 - lose_flag
    for u in rev_path_di[v]:
        unused_path_di[u].remove(v)
        if len(unused_path_di[u]) == 0 or dist[v] == 0:
            q.append(u)


for s in S:
    if dist[s[-3:]] == 1:
        print("Aoki")
    elif dist[s[-3:]] == 0:
        print("Takahashi")
    else:
        print("Draw")
