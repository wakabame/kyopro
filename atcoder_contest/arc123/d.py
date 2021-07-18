N = int(input())
A = list(map(int, input().split()))
if A[0] < 0:
    for i in range(N):
        A[i] = -A[i]
b, c = 0, 0

for i in range(N-1):
    diff = A[i+1] - A[i]
    if diff >= 0:
        b += diff
    else:
        c -= diff
ma = A[0] + max(b, c)
mi = 0

def return_by_height(c_st):
    # c の初期高さを c_st としたときのスコア
    c = - c_st
    b = A[0] - c_st
    ret = abs(b) + abs(c)
    for i in range(N-1):
        diff = A[i+1] - A[i]
        if diff >= 0:
            b += diff
        else:
            c -= diff
        ret += abs(b) + abs(c)
    return ret

# 三分探索により凸関数の最小値を算出する
def tripe_search(left, right):
    while abs(left-right) > 3:
        c1 = (2*left + right) // 3
        c2 = (left + 2*right) // 3
        d1 = return_by_height(c1)
        d2 = return_by_height(c2)
        if d1 < d2:
            right = c2
        elif d1 > d2:
            left = c1
        else:
            right = c2
            left = c1
    return left, right

left, right = tripe_search(mi, ma)
ans = return_by_height(right)
for i in range(left, right):
    ans = min(ans, return_by_height(i))
print(ans)
