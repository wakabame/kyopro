import sys
N, M, K = map(int, input().split())

if M == 1 :
    if K == N-1:
        print(1)
    else:
        print(0)
    sys.exit()

def power_func(a, n, p):
    bi = str(format(n,"b"))#2進表現に
    if a == 0:
        return 0
    res = 1
    for i in range(len(bi)):
        res = (res*res) % p
        if bi[i] == "1":
            res = (res*a) % p
    return res

P = 998244353
inv_t = [0] + [1]
for i in range(2, max(M,K)+2):
    inv_t += [inv_t[P % i] * (P - int(P / i)) % P]

ans = (M * power_func(M-1, N-1, P))%P
curr = ans
for k in range(K):
    curr = (curr*(N-k-1)*inv_t[k+1]*inv_t[M-1]) % P
    ans += curr
    ans %= P

print(ans)