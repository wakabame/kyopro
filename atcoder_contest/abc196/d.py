H, W, A, B = map(int, input().split())


table = [[False for w in range(W)] for h in range(H)]
ans = 0


def solve(table, a, b):
    # 全て埋まったときの処理
    if all([sum(table[i]) == W for i in range(H)]):
        if a == A and b == B:
            return 1
        else:
            return 0

    ret = 0
    for h in range(H):
        for w in range(W):
            if table[h][w] == True:
                # すでにタイルが詰められているなら次の座標に行く
                continue

            # 1 * 1 のタイルを詰める
            table_ = [[bool_ for bool_ in li] for li in table]
            table_[h][w] = True
            ret += solve(table_, a, b + 1)

            # 1 * 2 のタイルを詰める
            if w < W - 1 and table[h][w + 1] == False:
                table_ = [[bool_ for bool_ in li] for li in table]
                table_[h][w] = True
                table_[h][w + 1] = True
                ret += solve(table_, a + 1, b)
            # 2 * 1 のタイルを詰める
            if h < H - 1 and table[h + 1][w] == False:
                table_ = [[bool_ for bool_ in li] for li in table]
                table_[h][w] = True
                table_[h + 1][w] = True
                ret += solve(table_, a + 1, b)
            break
        else:
            continue
        break

    return ret


print(solve(table, 0, 0))
