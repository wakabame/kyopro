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


N = int(input())
a = list(map(int, input().split()))

BIT = Bit(N)
ans = 0
for i in range(N):
    ans += i - BIT.sum(a[i])
    BIT.add(a[i], 1)

print(ans)
