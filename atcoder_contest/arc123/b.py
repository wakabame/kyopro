N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

A.sort(reverse=True)
B.sort(reverse=True)
C.sort(reverse=True)
ans = 0
while A and B and C:
    a = A.pop()
    while B:
        b = B.pop()
        if b > a:
            break
    while C:
        c = C.pop()
        if c > b:
            break
    if c > b > a:
        ans += 1

print(ans)
