N = 100
X, Y = [], []
table = [[0 for i in range(N)] for j in range(N)]
for i in range(N):
    x, y = map(int, input().split())
    X += [x]
    Y += [y]
    table[x][y] = i

curr_x = 0
curr_y = 0
ans_str = ""


def move_x(curr_x, dx, ans_str):
    curr_x += dx
    if dx > 0:
        ans_str += "D" * dx
    else:
        ans_str += "U" * (-dx)

    return curr_x, ans_str


def move_y(curr_y, dy, ans_str):
    curr_y += dy
    if dy > 0:
        ans_str += "R" * dy
    else:
        ans_str += "L" * (-dy)

    return curr_y, ans_str


def move_and_append(curr_x, curr_y, i, ans_str):
    x, y = X[i], Y[i]

    if (i < N - 1 and curr_y == Y[i + 1]) and (curr_x - X[i + 1]) * (X[i + 1] - x) > 0:
        dx = X[i + 1] - curr_x
        curr_x, ans_str = move_x(curr_x, dx, ans_str)
        ans_str += "I"
        # TODO: 最後の空き地まで移動しておろす
        """
        table[curr_x][curr_y] = 0
        if dx > 0:# 下向き
            for x_ in range(X[i], X[i+1]+1):
                if table[x_][curr_y] == 0:
                    dx = x_ - curr_x
        curr_x, ans_str = move_x(curr_x, dx, ans_str)
        """
        ans_str += "O"
        # TODO: X[i+1] を書き換える
        table[curr_x][curr_y] = i + 1
        X[i + 1] = curr_x

        dx = X[i] - curr_x
        curr_x, ans_str = move_x(curr_x, dx, ans_str)
    else:
        dx = x - curr_x
        curr_x, ans_str = move_x(curr_x, dx, ans_str)

    if (i < N - 1 and curr_x == X[i + 1]) and (curr_y - Y[i + 1]) * (Y[i + 1] - y) > 0:
        dy = Y[i + 1] - curr_y
        curr_y, ans_str = move_y(curr_y, dy, ans_str)
        ans_str += "I"
        # TODO: 最後の空き地まで移動する
        ans_str += "O"
        # TODO: X[i+1] を書き換える
        dy = Y[i] - curr_y
        curr_y, ans_str = move_y(curr_y, dy, ans_str)
    else:
        dy = y - curr_y

        curr_y, ans_str = move_y(curr_y, dy, ans_str)

    return curr_x, curr_y, ans_str


for i in range(N):
    curr_x, curr_y, ans_str = move_and_append(curr_x, curr_y, i, ans_str)

    ans_str += "I"


print(ans_str)
# U .. x--
# D .. x++
# L .. y--
# R .. y++
# DDDDDDDDDDDDDDDRRRRRRRRRRRRRRRRRRRIUUUUUUULLLLLLLLLLLLLLLLLLIUUUUURRRRRRRRRRRRIURRRRRRIDDDDDDDDDDDDDDDLLLLLLLLLIUUULLLLLLLIUUUUUUUUUUULIDDDIDDDODDDDDDDDDDRRIUUUUUUUUUULLIDDDDDDDDDLIUUUUUUUUUUUUUURRRIURRRRRRIUUURRRRRIDDLLLLLLLLLLIDDDDDDDDRRIUUUULLLLIDDDDDDDDDDDDDRRRRRRRRRIUUUUUUUUUUUUUUUUUULLLLLLLLLLLLIDDDDDDDDDDDDDDDDDDRRRIUUUUUUUUUUUUUUULLIUUUURRRRRIDDDDDDDDDDRRRRRRRRRRRRIDDLLLLLLIUUUURIUULLLLLLLLLIDDDDLLIUUUURRRRRRRRRRIUUUULLLLLLLLLLLLIUURRRRRRRRRRRIDDDDDDLLIDDLLLLLLIDDDDDRRRRRRIUUUULLLLLLLLLIDDRRRRRRRRRRRRRRRRRIUULLLLLLLLLLLLLIDDDLLLIUUUUUUUUUUURRRRRRRRRRRRRRRRRIDDDDDDDDDDDDDDDDDDRIUUUUUUUUUULLLLLLLLLLIUUUUUUURRIDDDDDDRRRRRRRRIDDDDDDDDDDLLLLLLLLLLLLLLLLIUUUUUUUUUUUUUUUURRRRRRRRRRRRIDDDDDDRIDDDDDDDDLLLLLLLLLLLLLLIUUUUUUUUUUUURRRIDDDDDDDDDDLIUUUUULIDDDDDDRRRRRRRRRRIUUUUUUUUUUUULLLLLLLLLLLLLIDDDDDRRRRRRRRRRRIDDDDDDDLLLLLLLIUUUUUUUUUUUUUUURRRIDDDDDDDDDDDDRRRRRRRRRRRRIDDDDDDLLLLLLLLLLLLIUUUUUURRRRRRRRRRIUUUULLLLLLLLLLLLLLLIUULLIUUUUURRRRRRRIDDDDDDDDDDDDDDDDLLLLLLLIURRRRRRRRRRIUUUUUUUUUUUUUUULLLLIDDDDDDDDDLIUUUUUURRRRRRRRRIDDDDDDDDLLLLLLLIUUUUUURRRRILLLLLIDDDDDDDDRRRRRRRRRRRRRIDLLLLIDDRIUUUUUUUUUUUUUUUULLLLIDDDDDDLLLIUUUUULLIDDIUUULLLIDDDDLIUUUUURRRRRRRRRRRRRRIDDDDDDDDDDDDDDDDDLLLLLLLLLLLLLLIUUUUUUUUUUUURRRRRRRRRRIDDDDRRRIDDDLLLIULIDDDDRRRRRRIUUUUUUUUUUUUUUULLLLLLLLIDDDDDDDDDDDDDDDDDDDLLLLIUUUUUUULLIUURRRRIDDDDDLLLLLLLIUUUUURRRRRRRRRRRRIDDDDDDDRRIUUUUUUUUUUUUUUUULLLLLLLLLLIDDDDDDDDDDDDDDRRRRRRRRRIDDDDLLLLLLLLLIUURRIUUUUUUUUUUUUIUUUUUUUUUUUUODDDDDDDDDRRRRRRRRRRRIUUUUUUUUULLLLLLLLLLLIDDDDDDDDDDDDDDDDDDDLIUUUUUUUUUIDDDDDDDDDDDDDDDDRIUUUUUUUUUUUUUUUUUURRRRRRRRRI
