N, M = map(int, input().split())
path = [set() for i in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    path[a-1].add(b-1)
    path[b-1].add(a-1)
visited = [0] * N

ans = 1
for u in range(N):
    if visited[u] == 1:
        continue
    curr = 1
    visited[u] = 1
    next_u = path[u]
    while next_u:
        v = next_u.pop()
        if visited[v] == 1:
            continue
        visited[v] = 1
        curr += 1
        for w in path[v]:
            if visited[w] == 0:
                next_u.add(w)
    ans = max(ans, curr)

print(ans)