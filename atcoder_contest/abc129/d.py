H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]

cumsum_table = [[[0 for _ in range(W)] for _ in range(H)] for _ in range(4)]

for h in range(H):
    for w in range(W):
        if S[h][w] == "#":
            continue
        if h == 0:
            cumsum_table[0][h][w] = 1
        else:
            cumsum_table[0][h][w] = cumsum_table[0][h - 1][w] + 1

for h in range(H):
    for w in range(W):
        if S[h][w] == "#":
            continue
        if w == 0:
            cumsum_table[1][h][w] = 1
        else:
            cumsum_table[1][h][w] = cumsum_table[1][h][w - 1] + 1

for h in range(H)[::-1]:
    for w in range(W)[::-1]:
        if S[h][w] == "#":
            continue
        if h == H - 1:
            cumsum_table[2][h][w] = 1
        else:
            cumsum_table[2][h][w] = cumsum_table[2][h + 1][w] + 1

for h in range(H)[::-1]:
    for w in range(W)[::-1]:
        if S[h][w] == "#":
            continue
        if w == W - 1:
            cumsum_table[3][h][w] = 1
        else:
            cumsum_table[3][h][w] = cumsum_table[3][h][w + 1] + 1

ans = 0
for h in range(H):
    for w in range(W):
        ans = max(ans, sum([cumsum_table[i][h][w] for i in range(4)]) - 3)

print(ans)
