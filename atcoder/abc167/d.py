import sys
N, K = map(int, input().split())
A = list(map(int, input().split()))
for i in range(N):
    A[i] -= 1

visited = [1] + [0] * (N-1)
first_dist = [0] * N
turn = 0
pos = 0

for i in range(N+1):
    if i == K:
        print(pos+1)
        sys.exit()
    turn += 1
    pos = A[pos]
    if visited[pos] :
        loop = turn - first_dist[pos]
        break
    else:
        visited[pos] = 1
        first_dist[pos] = turn

loop_path = [pos]
for i in range(loop):
    pos = A[pos]
    loop_path.append(pos)
pos = loop_path.pop()
print(loop_path[(K - first_dist[pos])%loop] + 1)