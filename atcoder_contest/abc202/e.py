# DFSによるオイラーツアーを行い、頂点に初めて到達した時刻と頂点から戻る時刻をメモする
# x が y の親である iff in[x] < in[y] < out[y] < out[x] の関係にある
from bisect import bisect
import sys

sys.setrecursionlimit(20 ** 5)
N = int(input())
P = [s-1 for s in list(map(int, input().split()))]

edges = [[] for i in range(N)]
for i in range(N-1):
    edges[P[i]] += [i+1]

# i を出発点とする経路のリスト
time = 0
in_table = [0] * N
out_table = [0] * N
depth_intime_table = [[] for _ in range(N)]
def DFS(u=0, length=0):
    """
    頂点 u から出発するオイラーツアー
    """
    global time
    time += 1
    in_table[u] = time
    depth_intime_table[length] += [time]

    for v in edges[u]:
        DFS(v, length+1)
    time += 1
    out_table[u] = time
DFS()

Q = int(input())
for _ in range(Q):
    u, d = map(int, input().split())
    in_t = in_table[u-1]
    out_t = out_table[u-1]
    print(bisect(depth_intime_table[d], out_t)- bisect(depth_intime_table[d], in_t-1))
