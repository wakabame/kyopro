H, W = map(int, input().split())
S = [input() for _ in range(H)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def longest_BFS(h, w):
    ret = -1
    if S[h][w] == '#':
        return -1
    table = [[-1 for i in range(W)] for j in range(H)]
    table[h][w] = 0
    next_step = [[h, w]]
    while next_step:
        ret += 1
        step = next_step[:]
        next_step = []
        while step:
            u = step.pop()
            for i in range(4):
                if u[0]+dx[i] >= 0 and u[0]+dx[i] < H \
                    and u[1]+dy[i] >= 0 and u[1]+dy[i] < W \
                    and S[u[0]+dx[i]][u[1]+dy[i]] == '.' \
                    and table[u[0]+dx[i]][u[1]+dy[i]] == -1:
                    next_step += [[u[0]+dx[i], u[1]+dy[i]]]
                    table[u[0]+dx[i]][u[1]+dy[i]] = ret

    return ret

ans = 0
for h in range(H):
    for w in range(W):
        ans = max(ans, longest_BFS(h, w))
print(ans)

