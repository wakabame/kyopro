N = int(input())
S = input()

W_accum = [0]
E_accum = [0]
for i in range(N):
    if S[i] == "W":
        W_accum += [W_accum[-1] +1]
    else:
        W_accum += [W_accum[-1]]
    E_accum += [i+1 - W_accum[-1]]

ans = N
for i in range(N):
    curr = W_accum[i] + (E_accum[-1] - E_accum[i+1])
    ans = min(curr, ans)
print(ans)