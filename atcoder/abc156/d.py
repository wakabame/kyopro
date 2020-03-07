from functools import reduce

def comb(n, k, p):
  a = reduce(lambda x,y: x*y%p, range(n,n-k,-1))
  b = reduce(lambda x,y: x*y%p, range(1,k+1))
  return (a*pow(b, p-2, p))%p
      
n, a, b = map(int, input().split())
MOD = 10**9 + 7
     
print((pow(2,n,MOD) - 1 - comb(n, a, MOD) - comb(n, b, MOD))%MOD)