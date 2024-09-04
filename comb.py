def perm(n, k, p):
    ret = 1
    for i in range(n, n - k, -1):
        ret = (ret * i) % p
    return ret


def comb(n, k, p):
    a = perm(n, k, p)
    b = perm(k, k, p)
    return (a * pow(b, -1, p)) % p
