N = int(input())
a = list(map(int, input().split()))

st = 0
gl = 0
curr = a[0]
ans = 0
while True:
    if curr == N:
        ans += 1
        curr -= a[st]
        st += 1
    elif curr <= N:
        if gl == N - 1:
            break
        curr += a[gl + 1]
        gl += 1
    elif curr >= N:
        curr -= a[st]
        st += 1
print(ans)
