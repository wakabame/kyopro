def power_func(a, n, p):
  """
  power function under modulation
  a: 指数の低
  n: 累乗
  p: modulation
  """
  bi=str(format(n,"b"))#2進表現に
  res=1
  for i in range(len(bi)):
    res=(res*res) %p
    if bi[i]=="1":
      res=(res*a) %p
  return res

MOD = 10**9+7
N = int(input())
A = list(map(int, input().split()))

A.sort()
if N%2:
  correct = [0]
  for i in range(N//2):
    correct += [(i+1)*2]*2
else:
  correct = []
  for i in range(N//2):
    correct += [i*2+1]*2
if A == correct:
  print(power_func(2, N//2, MOD))
else:
  print(0)