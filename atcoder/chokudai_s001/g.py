N = int(input())
a = list(map(int, input().split()))
a.reverse()

keta = 0
ans = 0
MOD = 10**9 + 7
mod_to_digit = []
curr = 1
for i in range(1, 10**6):
    mod_to_digit.append(curr)
    curr = (curr*10)%MOD 
for i in range(N):
    ans += (a[i]*(mod_to_digit[keta]))%MOD
    keta += len(str(a[i]))

print(ans%(10**9+7))