N = int(input())
A = list(map(int, input().split()))

Li = [0] * max(A)
for a in A:
    Li[a - 1] += 1

ans = sum(a * (a - 1) // 2 for a in Li)

for a in A:
    print(ans - (Li[a - 1] - 1))
