N = int(input())
A = tuple(map(int, input().split()))

def return_by_pay(x):
    ret = 0
    for i in range(N):
        ret += x + A[i] - min(A[i], 2*x)

    return ret

# 三分探索により凸関数の最小値を算出する
def tripe_search(left, right):
    while abs(right - left)/right > 1e-8:
        c1 = (2*left + right) / 3
        c2 = (left + 2*right) / 3
        d1 = return_by_pay(c1)
        d2 = return_by_pay(c2)
        if d1 < d2:
            right = c2
        elif d1 > d2:
            left = c1
        else:
            right = c2
            left = c1
    return (left + right) / 2

best_cost = tripe_search(0, 10**9)
print(return_by_pay(best_cost)/N)
