N = int(input())
A = list(map(int, input().split()))

flag = 1
for i in range(N):
    if A[i] % 2 == 1:
        continue
    elif A[i] % 3 == 0:
        continue
    elif A[i] % 5 == 0:
        continue
    else:
        flag = 0

if flag:
    print("APPROVED")
else:
    print("DENIED")
