N, X, Y = map(int, input().split())

ans_list = [0] * N
for i in range(N):
    for j in range(i+1,N):
        curr = min(j-i, abs(X-i-1) + 1 + abs(Y-j-1))
        ans_list[curr] += 1

for i in range(1,N):
    print(ans_list[i])