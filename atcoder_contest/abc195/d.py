N, M, Q = map(int, input().split())
WV = []
for _ in range(N):
    WV += [tuple(map(int, input().split()))]
X = list(map(int, input().split()))

WV.sort(key=lambda x: -x[1])

for _ in range(Q):
    L, R = map(int, input().split())
    boxes = X[:L-1] + X[R:]
    boxes.sort()
    used = [False] * len(boxes)

    pointer = 0
    curr = 0
    for weight, value in WV:
        # 価値の大きい順に
        for i in range(len(boxes)):
            if boxes[i] >= weight and used[i] == False:
                curr += value
                used[i] = True
                break

    print(curr)