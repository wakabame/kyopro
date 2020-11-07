from collections import deque
N, M = map(int, input().split())
path = [[] for i in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    path[a-1] += [b-1]
    path[b-1] += [a-1]

next_vec = [0]
visited = [1] + [0] * (N-1)
parent = [-1] + [0] * (N-1)
flag = 1


while next_vec:
    current_vec = next_vec[:]
    next_vec = []
    while current_vec:
        u = current_vec.pop()
        visited[u] = 1
        for v in path[u]:
            if visited[v] == 0:
                visited[v] = 1
                parent[v] = u
                next_vec.append(v)

ans_flag = 1
for i in visited:
    if i == 0:
        ans_flag = 0
if ans_flag:
    print('Yes')
    for i in range(1,N):
        print(parent[i]+1)
else:
    print('No')
