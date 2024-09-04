N = int(input())
pulls = []
minus = []

for _ in range(N):
    x, y = map(int, input().split())
    pulls += [x + y]
    minus += [x - y]

pulls.sort()
minus.sort()
print(max(pulls[-1] - pulls[0], minus[-1] - minus[0]))
