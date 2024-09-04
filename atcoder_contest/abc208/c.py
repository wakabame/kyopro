N, K = map(int, input().split())
A = list(map(int, input().split()))

li = [[a, i, 0] for i, a in enumerate(A)]

li.sort()
shou, amari = K // N, K % N
for i in range(N):
    li[i][2] = shou
for i in range(amari):
    li[i][2] += 1

li.sort(key=lambda x: x[1])

for a, i, coin in li:
    print(coin)
