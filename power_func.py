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