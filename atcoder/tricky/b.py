# 丸め誤差を抑えるために逆有理化
T = int(input())
ABC = [[int(x) for x in input().split()] for _ in range(T)]

for a, b, c in ABC:
  if a == 0:
    if b == 0:
      if c == 0:
        print(3)
      else:
        print(0)
    else:
      print(1, -c/b)
  else:
    if a < 0: # aの符号で悩みたくない
      a, b, c = -a, -b, -c
    D = b**2 - 4*a*c
    if D <0:
      print(0)
    elif D == 0:
      print(1, -b/(2*a))
    else:
      d = D**.5
      if b >= 0:
        print(2, 
             (-b-d)/(2*a),
             -2*c/(b+d)
             )
      else:
        print(2, 
             -2*c/(b-d),
             (-b+d)/(2*a)
             )
        