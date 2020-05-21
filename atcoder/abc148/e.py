N = int(input())

if N%2:
    ans = 0
else:
    ans = 0
    while N > 1:
        N = N//5
        ans += N//2

print(ans)