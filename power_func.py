def power_func(a, n, p):
    """
    power function under modulation
    a: 指数の低
    n: 累乗
    p: modulation
    treat: 0^0 = 0 
    """
    bi = str(format(n,"b"))#2進表現に
    if a == 0:
        return 0
    res = 1
    for i in range(len(bi)):
        res = (res*res) % p
        if bi[i] == "1":
            res = (res*a) % p
    return res