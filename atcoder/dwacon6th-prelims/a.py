N = int(input())
music = []
for _ in range(N):
    s, t = map(str, input().split())
    music.append([s, int(t)])
number = input()

ans = 0
flag = False
for i in range(N):
    if flag:
        ans += music[i][1]
    elif number == music[i][0]:
        flag = True 

print(ans)