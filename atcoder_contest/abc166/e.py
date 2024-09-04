N = int(input())
A = list(map(int, input().split()))

up_lift = [0] * N
down_lift = [0] * N
for i in range(N):
    if i + A[i] < N:
        up_lift[i + A[i]] += 1
    if i - A[i] >= 0:
        down_lift[i - A[i]] += 1

ans = 0
for i in range(N):
    ans += up_lift[i] * down_lift[i]
print(ans)
