N, K = map(int, input().split())
p = list(map(int, input().split()))

best_score = 0
for i in range(K):
    best_score += p[i] + 1

curr = best_score
for i in range(N - K):
    curr += p[i + K] + 1
    curr -= p[i] + 1
    if curr > best_score:
        best_score = curr

print(best_score / 2)
