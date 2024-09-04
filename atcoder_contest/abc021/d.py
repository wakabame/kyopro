n = int(input())
k = int(input())

P = 10**9 + 7
fac = [1] + [1]
finv = [1] + [1]
inv = [0] + [1]

for i in range(2, n + k + 1):
    fac += [fac[-1] * i % P]
    inv += [P - inv[P % i] * (P // i) % P]
    finv += [finv[-1] * inv[i] % P]


def comb(n, k):
    if n < 0 or k < 0 or n < k:
        return 0
    return fac[n] * finv[k] * finv[n - k] % P


print(comb(n + k - 1, k))
