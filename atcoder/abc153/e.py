# E - Crested Ibis vs Monster
H, N = map(int, input().split())
AB = []
for i in range(N):
    a, b = map(int, input().split())
    AB.append((a,b))

max_a = max(AB[i][0] for i in range(N))
DP = [10**18 for i in range(H + max_a + 1)]
DP[0] = 0
for i in range(1, H + max_a):
    DP[i] = min(DP[i - a] + b for a, b in AB)

print(min(DP[H:]))
