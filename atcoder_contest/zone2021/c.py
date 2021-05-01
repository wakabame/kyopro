N = int(input())

scores = []
maxes = [0]*5
for _ in range(N):
    scores += [tuple(map(int, input().split()))]
    for i in range(5):
        maxes[i] = max(maxes[i], scores[-1][i])

def is_ok(mid):
    # 二人選んできて、mid未満の科目が1個まで
    # 残りの科目のmax がmid以上ならOK
    for i in range(N):
        short_flag = [True]*5
        for k in range(5):
            if scores[i][k] >= mid:
                short_flag[k] = False
        if sum(short_flag) >= 4:
            continue
        for j in range(i):
            short_flag_ = short_flag[:]
            for k in range(5):
                if scores[j][k] >= mid:
                    short_flag_[k] = False
            if sum(short_flag_) == 0:
                return True
            elif sum(short_flag_) == 1:
                for k in range(5):
                    if short_flag_[k] and maxes[k] >= mid:
                        return True
    return False

# 汎用的な二分探索のテンプレ
def binary_search(ok, ng):
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok

ok = 0
ng = 10**9 +1

print(binary_search(ok, ng))
