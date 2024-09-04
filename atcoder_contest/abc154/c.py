N, K = map(int, input().split())
A = list(map(int, input().split()))
st = set(A)
if len(st) == N:
    print("YES")
else:
    print("NO")
