from collections import deque
import itertools

H, W = map(int, input().split())
C_h, C_w = map(int, input().split())
D_h, D_w = map(int, input().split())

S = [input() for _ in range(H)]
dist = [[-1 for i in range(W)] for j in range(H)]
dist[C_h - 1][C_w - 1] = 0
arrived = [[0 for i in range(W)] for j in range(H)]
arrived[C_h - 1][C_w - 1] = 1

d = deque([[C_h - 1, C_w - 1, 0]])


def check_movable(h, w):
    if h < 0 or h >= H or w < 0 or w >= W:
        return False
    elif S[h][w] == "#":
        return False
    elif arrived[h][w] == True:
        return False
    else:
        return True


def check_appnendable(h, w, cost):
    if not check_movable(h, w):
        return False
    if dist[h][w] == -1:
        return True
    elif dist[h][w] > cost:
        return True
    else:
        return False


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
while d:
    h, w, cost = d.pop()
    if cost > dist[h][w] and dist[h][w] != -1:
        continue
    for dh, dw in zip(dx, dy):
        if check_appnendable(h + dh, w + dw, cost):
            d.append([h + dh, w + dw, cost])
            dist[h + dh][w + dw] = cost
            arrived[h + dh][w + dw] = True
    for dh, dw in itertools.product(range(-2, 3), range(-2, 3)):
        if check_appnendable(h + dh, w + dw, cost + 1):
            d.appendleft([h + dh, w + dw, cost + 1])
            dist[h + dh][w + dw] = cost + 1

print(dist[D_h - 1][D_w - 1])
