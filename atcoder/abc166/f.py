N, *ABC = map(int, input().split())
s = [input() for _ in range(N)]

yes_flag = True
ans_list = []

if sum(ABC) == 0:
    yes_flag = False

for i in range(N):
    if not yes_flag:
        break
    u = ord(s[i][0]) - 65
    v = ord(s[i][1]) - 65
    if ABC[u] + ABC[v] == 0:
        yes_flag = False
    elif ABC[u] + ABC[v] == 1:
        if ABC[u] == 1:
            ans_list += [s[i][1]]
            ABC[u] -= 1
            ABC[v] += 1
        else:
            ans_list += [s[i][0]]
            ABC[v] -= 1
            ABC[u] += 1
    elif ABC[u] + ABC[v] == 2:
        # 両方1の場合だけケアが必要
        if ABC[u] * ABC[v] == 1:
            if i == N-1:
                if ABC[u] > 0:
                    ans_list += [s[i][1]]
                else:
                    ans_list += [s[i][0]]
            else:
                if s[i][1] in s[i+1]:
                    ans_list += [s[i][1]]
                    ABC[u] -= 1
                    ABC[v] += 1
                else:
                    ans_list += [s[i][0]]
                    ABC[v] -= 1
                    ABC[u] += 1
        else:
            if ABC[u] > 1:
                ans_list += [s[i][1]]
                ABC[u] -= 1
                ABC[v] += 1
            else:
                ans_list += [s[i][0]]
                ABC[v] -= 1
                ABC[u] += 1
    else:
        if ABC[u] > 1:
            ans_list += [s[i][1]]
            ABC[u] -= 1
            ABC[v] += 1
        else:
            ans_list += [s[i][0]]
            ABC[v] -= 1
            ABC[u] += 1

if yes_flag:
    print("Yes")
    print(*ans_list)
else:
    print("No")
