from math import pi, sin

EPS = 10 ** (-7)
A, B, C = map(int, input().split())


def dist_from_100(t):
    return A * t + B * sin(C * t * pi) - 100


def is_ok(mid):
    # At + Bsin(C\pi t)) - 100 が非負ならばok
    return dist_from_100(mid) >= 0


# 汎用的な二分探索のテンプレ
# f(t)-100 の零点は1つ以上考えられるが、平均値の定理から零点のうちのどれか一つに収束する
def binary_search(ok, ng):
    dist = dist_from_100(ok)
    while dist > EPS:
        mid = (ok + ng) / 2
        if is_ok(mid):
            ok = mid
            dist = dist_from_100(ok)
        else:
            ng = mid
    return ok


ok = 200
ng = 0

print(binary_search(ok, ng))
