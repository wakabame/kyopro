from math import gcd
N, M = map(int, input().split())
AC = [list(map(int, input().split())) for _ in range(M)]
AC.sort(key=lambda x:x[1])

# クラスカル法 ... コストがちっちゃい path から貪欲に追加していく
ans = 0
for a, c in AC:
    a = gcd(N, a)
    # 幅 a の橋をできるだけ作る
    ans += (N-a) * c
    N = a # 状態数はa個にまとめられる

# 状態が一つになる <=> 全域木ができた
if N == 1:
    print(ans)
else:
    print(-1)
