def perm(n, k, p):
  ret = 1
  for i in range(n, n-k, -1):
    ret = (ret * i)%p
  return ret

def comb(n, k, p):
  a = perm(n, k, p)
  b = perm(k, k, p)
  return (a*pow(b, -1, p))%p

S = int(input())

ans = 0
S -= 3
t = 0
while S >= 0:
    ans += comb(S+t,t, 10**9+7)
    S -= 3
    t += 1

print(ans%(10**9+7))