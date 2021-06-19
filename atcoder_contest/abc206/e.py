L, R = map(int, input().split())

gcd_is_g = [0 for g in range(R+1)]
# gcd_is_g[g] ... [L, R] に含まれる x, y であって, 最大公約数が g となるもの
# g > R のとき, gcd_is_g[g] = 0

for g in range(1,R+1)[::-1]:
  st, en = (L-1)//g, R//g
  # まずは最大公約数が g の倍数となるものを求める
  gcd_is_g[g] = (en - st) **2

  c = 2
  # gcd_is_g[c*g] ... 最大公約数が 2*g となるものを除いていく
  while g*c < R+1:
    gcd_is_g[g] -= gcd_is_g[g*c]
    c += 1

ans = 0
# gcd_is_g[1] は答えに影響しない
for g in range(2,R+1):
  st, en = (L-1)//g, R//g

  # x, y のいずれかが g になる場合をここで除く
  if L <= g <= R:
    gcd_is_g[g] -= (en - st) * 2 - 1
  ans += gcd_is_g[g]

print(ans)
