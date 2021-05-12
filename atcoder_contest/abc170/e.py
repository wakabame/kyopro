class SegTree:
    """
    init(init_val, ide_ele): 配列init_valで初期化 O(N)
    update(k, x): k番目の値をxに更新 O(N)
    query(l, r): 区間[l, r)をsegfuncしたものを返す O(logN)
    """

    def __init__(self, init_val, segfunc, ide_ele):
        """
        init_val: 配列の初期値
        segfunc: 区間にしたい操作
        ide_ele: 単位元
        n: 要素数
        num: n以上の最小の2のべき乗
        tree: セグメント木(1-index)
        """
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1 << (n - 1).bit_length()
        self.tree = [ide_ele] * 2 * self.num
        # 配列の値を葉にセット
        for i in range(n):
            self.tree[self.num + i] = init_val[i]
        # 構築していく
        for i in range(self.num - 1, 0, -1):
            self.tree[i] = self.segfunc(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, k, x):
        """
        k番目の値をxに更新
        k: index(0-index)
        x: update value
        """
        k += self.num
        self.tree[k] = x
        while k > 1:
            self.tree[k >> 1] = self.segfunc(self.tree[k], self.tree[k ^ 1])
            k >>= 1

    def query(self, l, r):
        """
        [l, r)のsegfuncしたものを得る
        l: index(0-index)
        r: index(0-index)
        """
        res = self.ide_ele

        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                res = self.segfunc(res, self.tree[l])
                l += 1
            if r & 1:
                res = self.segfunc(res, self.tree[r - 1])
            l >>= 1
            r >>= 1
        return res


import heapq
from collections import defaultdict

N, Q = map(int, input().split())
b_max = 2 * (10 ** 5)
infant_rates = []
class_dict = [defaultdict(int) for _ in range(b_max)]
class_scores_hq = [[] for _ in range(b_max)]

di = {}  # 幼児 k はどこの組に居るか

for k in range(N):
    a, b = map(int, input().split())
    infant_rates += [a]
    heapq.heappush(class_scores_hq[b - 1], -a)
    class_dict[b - 1][a] += 1
    di[k] = b - 1

segtree_list = []
for i in range(b_max):
    if class_scores_hq[i]:
        segtree_list += [-class_scores_hq[i][0]]
    else:
        segtree_list += [float("INF")]
segtree = SegTree(segtree_list, min, float("INF"))

for _ in range(Q):
    c, d = map(int, input().split())
    infant_score = infant_rates[c - 1]
    before_belong = di[c - 1]

    # 幼児の所属の更新
    di[c - 1] = d - 1

    # 前所属からの削除
    class_dict[before_belong][infant_score] -= 1
    while len(class_scores_hq[before_belong]) > 0:
        if class_dict[before_belong][-class_scores_hq[before_belong][0]] == 0:
            heapq.heappop(class_scores_hq[before_belong])
        else:
            break

    if len(class_scores_hq[before_belong]) > 0:
        segtree.update(before_belong, -class_scores_hq[before_belong][0])
    else:
        segtree.update(before_belong, float("INF"))

    # 次所属の更新
    heapq.heappush(class_scores_hq[d - 1], -infant_score)
    class_dict[d - 1][infant_score] += 1
    segtree.update(d - 1, -class_scores_hq[d - 1][0])

    print(segtree.query(0, b_max))
