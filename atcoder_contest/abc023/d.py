N = int(input())
H, S = [], []
for _ in range(N):
    h, s = map(int, input().split())
    H.append(h)
    S.append(s)


def is_ok(mid):
    # k 秒経過したとき, i 番目の風船のペナルティは H[i] + k * S[i]
    # ペナルティを mid 以下に抑えるには, k <= (mid - H[i]) // S[i] 秒以内に撃ち落とす必要がある
    time_limits = []
    for i in range(N):
        time_limits += [(mid - H[i]) // S[i]]
    time_limits.sort()
    for i in range(N):
        if time_limits[i] < i:
            return False
    return True


# 汎用的な二分探索のテンプレ
def binary_search(ok, ng):
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok


ok = max(H) + N * max(S)
ng = -1

print(binary_search(ok, ng))
