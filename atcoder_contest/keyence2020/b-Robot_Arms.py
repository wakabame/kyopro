N = int(input())
segment = []

for _ in range(N):
    x, l = map(int, input().split())
    segment.append([max(0, x-l), x+l])

segment.sort(key=lambda seg: seg[1])

ans = 0
curr_time = -1

for i in range(N):
    if curr_time < segment[i][0]:
        curr_time = segment[i][1] - 1
        ans += 1

print(ans)