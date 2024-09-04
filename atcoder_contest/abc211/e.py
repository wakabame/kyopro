from collections import defaultdict

N = int(input())
K = int(input())

S = [list(input()) for _ in range(N)]

dh = [1, -1, 0, 0]
dw = [0, 0, 1, -1]

length_to_set = defaultdict(set)
for h in range(N):
    for w in range(N):
        if S[h][w] == ".":
            length_to_set[0].add((frozenset({(h, w)})))

for k in range(K - 1):
    for path in length_to_set[k]:
        for h, w in path:
            for i in range(4):
                h_ = h + dh[i]
                w_ = w + dw[i]
                if (h_, w_) in path:
                    continue
                if h_ < 0 or h_ >= N or w_ < 0 or w_ >= N:
                    continue
                if S[h_][w_] == "#":
                    continue
                path_ = set(path)
                path_.add((h_, w_))
                length_to_set[k + 1].add(frozenset(path_))

print(len(length_to_set[K - 1]))
