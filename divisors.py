def divisors(n):
    ret1 = []
    ret2 = []
    i = 1
    while i**2 <= n:
        if i**2 == n:
            ret1 += [i]
        elif n % i == 0:
            ret1 += [i]
            ret2 += [n // i]
        i += 1
    ret2.reverse()
    return ret1 + ret2
    # nの約数を列挙するO(n^{1/2})
