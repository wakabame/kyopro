from collections import Counter

n = int(input())
v = list(map(int, input().split()))

cnt1 = Counter(v[::2]).most_common()
cnt2 = Counter(v[1::2]).most_common()
cnt1 += [(-1,0)]
cnt2 += [(-1,0)]
if cnt1[0][0] != cnt2[0][0]:
    print(n - (cnt1[0][1] + cnt2[0][1]))
else:
    print(n - max(cnt1[1][1] + cnt2[0][1], cnt1[0][1] + cnt2[1][1]))