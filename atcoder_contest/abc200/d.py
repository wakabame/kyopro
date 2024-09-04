N = int(input())
A = list(map(int, input().split()))

rem_list = [[] for _ in range(200)]
k = min(N, 8)
for i in range(1, 1 << k):
    curr = 0
    for j in range(k):
        if i & (1 << j):
            curr += A[j]
            curr %= 200
    st = "{:08b}".format(i)[-k:][::-1]
    li = []
    for j in range(k):
        if st[j] == "1":
            li += [j + 1]
    rem_list[curr] += [li]

for i in range(200):
    if len(rem_list[i]) > 1:
        print("Yes")
        print(len(rem_list[i][0]), *rem_list[i][0])
        print(len(rem_list[i][1]), *rem_list[i][1])
        exit()
print("No")
