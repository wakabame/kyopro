class Bit:
    """
    Binary Indexed Tree (BIT)
    Bit(n) n 要素の変数
    sum(i) i 番目までの和...log(n)
    add(i, x) i番目の要素にxを加える...log(n)
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


N, Q = map(int, input().split())
A = list(map(int, input().split()))

bit = Bit(N)
for i, a in enumerate(A):
    bit.add(i + 1, a)

for _ in range(Q):
    t, x, y = map(int, input().split())
    if t == 0:
        bit.add(x + 1, y)
    elif t == 1:
        print(bit.sum(y) - bit.sum(x))
