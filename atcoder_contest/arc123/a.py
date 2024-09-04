A = list(map(int, input().split()))
sa1 = A[1] - A[0]
sa2 = A[2] - A[1]

ans = float("inf")
# A[0] を固定する場合
## A[2] を固定する場合
if sa2 >= sa1:
    ans = (sa2 - sa1) // 2 + (sa2 - sa1) % 2 * 2
if sa2 < sa1:
    ans = min(sa1 - sa2, ans)
# A[1] を固定する場合
ans = min(ans, abs(sa1 - sa2))
print(ans)
