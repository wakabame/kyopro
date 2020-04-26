S = input()
N = len(S)
table = [1] + [0] * 2020
exp = [1]
for i in range(N):
    exp += [exp[-1]*10 %2019]

curr = 0
for i in range(N):
    curr += int(S[N-1-i])*exp[i]
    curr %= 2019
    table[curr] += 1

ans = 0
for i in table:
    ans += i*(i-1)//2
print(ans)