N = int(input())
K = int(input())
L = len(str(N))

suu = []
for i in range(L):
    suu.append(int(str(N)[i]))

DP_1 =[[0 for k in range(L+2)] for i in range(L+1)]
DP_2 =[[0 for k in range(L+2)] for i in range(L+1)]
DP_2[0][0] = 1
for i in range(L):
    for k in range(L+1):
        DP_1[i+1][k] = DP_1[i][k] + DP_1[i][k-1] * 9 
        if suu[i]:
            DP_1[i+1][k] += DP_2[i][k] + DP_2[i][k-1] * max(suu[i] - 1, 0)
            DP_2[i+1][k] = DP_2[i][k-1]
        else:
            DP_2[i+1][k] = DP_2[i][k]
print(DP_1[L][K]+ DP_2[L][K])