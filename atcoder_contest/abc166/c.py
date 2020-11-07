N, M = map(int, input().split())
H = list(map(int, input().split()))
highest = [True for i in range(N)]

for i in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    if H[a] <= H[b]:
        highest[a] = False
    if H[b] <= H[a]:
        highest[b] = False

print(sum(highest))