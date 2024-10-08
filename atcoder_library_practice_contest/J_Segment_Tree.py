N, Q = map(int, input().split())
A = list(map(int, input().split()))


class SegTree:
    """
    __init__(init_val): 配列init_valで初期化 O(N)
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
        [l, r) のsegfuncしたものを得る
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


segtree = SegTree(A, max, -float("INF"))
ans = []
for _ in range(Q):
    t, x, y = map(int, input().split())

    if t == 1:
        # x-1 の一点更新
        segtree.update(x - 1, y)

    elif t == 2:
        # [x-1, y) の最大値
        ans += [segtree.query(x - 1, y)]

    elif t == 3:
        # [x-1, end) であって, value が y 以上の index
        start = x - 1
        end = N + 1
        while end - start > 1:
            mid = (start + end) // 2
            if segtree.query(start, mid) < y:
                start = mid
            else:
                end = mid
        ans += [start + 1]
print(*ans)
