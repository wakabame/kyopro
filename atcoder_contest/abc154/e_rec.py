N = int(input())
K = int(input())
L = len(str(N))


def solve(num_str, k, smaller):
    if num_str == "" and k > 0:
        return 0
    if k == 0 or num_str == "":
        return 1

    elif smaller:
        keta = len(num_str)
        if k == 1:
            return keta * 9
        elif k == 2:
            return keta * (keta - 1) // 2 * 9 * 9
        else:
            return keta * (keta - 1) * (keta - 2) // 6 * 9 * 9 * 9
    else:
        num = int(num_str)
        num_str = str(num_str)
        top = int(num_str[0])
        if top:
            zero = solve(num_str[1:], k, True)
            non_zero = solve(num_str[1:], k - 1, True) * (top - 1)
            just = solve(num_str[1:], k - 1, False)
            return zero + non_zero + just
        else:
            return solve(num_str[1:], k, False)


print(solve(str(N), K, False))
