N = int(input())
a = list(map(int, input().split()))

curr = 0
ans = 0
for i in range(N):
    if curr < a[i]:
        ans += 1
        curr = a[i]
print(ans)