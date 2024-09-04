N = int(input())
L = list(map(int, input().split()))
L.sort(reverse=True)
L_ = []
for i in range(N):
    L_ += [L[i] * (10**3) + (N - i - 1)]
# length_list[m] m 以下の長さの辺の個数
length_list = [0] * (10**3 + 1)
for i in range(N):
    length_list[L[i]] += 1
for i in range(10**3):
    length_list[i + 1] += length_list[i]

length_list_ = [0] * (2 * 10**6 + 1)
for i in range(N):
    length_list_[L_[i]] += 1
for i in range(2 * 10**6):
    length_list_[i + 1] += length_list_[i]

ans = 0
for i in range(N):
    for j in range(i + 1, N):
        ans += max(0, length_list_[L_[j] - 1] - length_list[(L[i] - L[j])])
print(ans)
