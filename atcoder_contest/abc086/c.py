N = int(input())
X, Y, T = 0, 0, 0
flag = True

for _ in range(N):
    t, x, y = map(int, input().split())
    duration = t - T
    x_diff = x - X
    y_diff = y - Y
    if abs(x_diff) + abs(y_diff) > duration:
        flag = False
    if (x_diff + y_diff + duration) % 2:
        flag = False
    X = x
    Y = y
    T = t

if flag:
    print("Yes")
else:
    print("No")
