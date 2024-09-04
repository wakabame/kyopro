def perm(n, k, p):
    ret = 1
    for i in range(n, n - k, -1):
        ret = (ret * i) % p
    return ret


def comb(n, k, p):
    a = perm(n, k, p)
    b = perm(k, k, p)
    return (a * pow(b, p - 2, p)) % p


n, a, b = map(int, input().split())

MOD = 10**9 + 7

print((pow(2, n, MOD) - 1 - comb(n, a, MOD) - comb(n, b, MOD)) % MOD)
