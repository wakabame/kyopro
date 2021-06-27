N = int(input())
if N == 1:
    exit(print("Yes"))

ab = [complex(*map(int, input().split())) for _ in range(N)]
cd = [complex(*map(int, input().split())) for _ in range(N)]

# 2 群を重心が原点になるように平行移動
ab = [ab[n] * N - sum(ab) for n in range(N)]
cd = [cd[n] * N - sum(cd) for n in range(N)]
if cd[0] == 0:
    cd[0], cd[1] = cd[1], cd[0]

for i in range(N):
    # ab[i] と cd[0] のなす角を求めて, cd をその角度回転させる
    if abs(ab[i]) != abs(cd[0]):
        continue
    theta = ab[i] / cd[0]
    target = [cd[i] * theta for i in range(N)]

    all_ok = True
    for k in range(N):
        k_is_ok = False
        for j in range(N):
            if abs(ab[j] - target[k]) < 0.1:
                k_is_ok = True
                break
        all_ok &= k_is_ok
    if all_ok:
        print("Yes")
        break
else:
    print("No")
