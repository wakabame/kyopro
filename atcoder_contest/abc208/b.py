P = int(input())
ans = 0

while P:
  curr = 1
  p = 1
  while True:
    if curr * (p+1) > P:
      P -= curr
      ans += 1
      break
    else:
      curr *= (p+1)
      p += 1
print(ans)
