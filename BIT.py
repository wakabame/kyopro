class Bit:
    """
    Binary Indexed Tree (BIT)
    Bit(n) n 要素の変数
    sum(i) i 番目までの和...log(n)
    add(i, x) i番目の要素にxを加える...log(n)
      1-indexed であることに注意する(区緩和のbit演算のため)
    """

    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s

    def add(self, i, x):
        while i <= self.size:
            self.tree[i] += x
            i += i & -i
